import os
from datetime import datetime
from .KiprisDataCartridge import KiprisDataCartridge
from .KiprisXmlToDictConverter import KiprisXmlToDictConverter
from ...convert.mapper.KiprisIpcXmlMapper import KiprisIpcXmlMapper
from ...convert.mapper.KiprisPriorityXmlMapper import KiprisPriorityXmlMapper
from ....db.mysql import Mysql

class KiprisXmlDumpDataQueryBuilder():
    def __init__(
        self, 
        table_name:str="table_name", 
        xml_filename:str="xml_filename",
        xml_to_dict_converter_class:type[KiprisXmlToDictConverter] = KiprisXmlToDictConverter,
        chunk_size: int = 1000
    ):
        self.data = []
        self.table_name = table_name
        self.service_type = table_name.split("_")[-1]
        self.org_type = table_name.split("_")[1]
        self.xml_to_dict_converter:KiprisXmlToDictConverter = xml_to_dict_converter_class(xml_filename=xml_filename)
        self.xml_to_dict_converter.service_type = self.service_type
        self.xml_to_dict_list = self.xml_to_dict_converter.parse()
        self.chunk_size = chunk_size
        self.sub_dict_list = self.xml_to_dict_converter.sub_dict_list

    def __get_mapper_dict(self):
        return self.xml_to_dict_converter.mapper.get_dict_with_properties()
    
    def __get_insert_info(self):

        columns = list(self.__get_mapper_dict().keys())
        if self.service_type in ['design', 'trademark']:
            columns.remove("priority_date")
            columns.remove("priority_no")
        columns = ", ".join(columns)
        return f"INSERT INTO kipris.{self.table_name} ({columns})"
    
    def __get_upsert_info(self):
        
        upsert_query = "ON DUPLICATE KEY UPDATE \n"

        additional_update_clause = ""

        if self.table_name in ["TB24_design", "TB2_patent"]:
            additional_update_clause = """
            reg_no = VALUES(reg_no),
            reg_date = VALUES(reg_date),
            open_no = VALUES(open_no),
            open_date = VALUES(open_date),
        """ 
        
        common_update_clause = """
            legal_status_desc = VALUES(legal_status_desc),
            pub_num = VALUES(pub_num),
            pub_date = VALUES(pub_date);
        """

        return upsert_query + additional_update_clause + common_update_clause

    def __get_upsert_sub_info(self):

        if self.service_type in ['design', 'trademark']:
            upsert_query = """
                ON DUPLICATE KEY UPDATE
                priority_date = VALUES(priority_date),
                priority_no = VALUES(priority_no);
            """

            return upsert_query
        else: 
            upsert_query = """
                ON DUPLICATE KEY UPDATE 
                ipc_cpc_code = ipc_cpc_code;
            """
        
        return upsert_query
    
    def __get_sub_insert_info(self):
        columns = ", ".join(self.__get_mapper_dict())
        service_number = 10 if self.service_type == 'patent' else 20
        return f"INSERT INTO kipris.TB24_3{service_number}_{self.org_type} ({columns}) \nSELECT"

    def append(self, data:KiprisDataCartridge):
        self.data.append(tuple(data.get_dict_with_properties().values()))

    def value_fillter(self, value):
        if isinstance(value, str) and len(value) == 8 and value.isdigit():
            try:
                value = datetime.strptime(value, '%Y%m%d').strftime("'%Y-%m-%d'")
            except ValueError:
                pass
        # None 값 처리
        elif value is None:
            value = 'NULL'
        # 문자열 값 처리 (이스케이프 처리)
        elif isinstance(value, str):
            value = f"'{value.replace("'", "''")}'"  # 작은따옴표 이스케이프
        else:
            value = str(value)

        return value

    def get_chunked_sql_files(self):
        insert_info = f"{self.__get_insert_info()}\nVALUES\n"
        chunked_data = []
        
        for i in range(0, len(self.xml_to_dict_list), self.chunk_size):
            chunk_data = [insert_info]
            
            for j, xml_to_dict in enumerate(self.xml_to_dict_list[i:i + self.chunk_size]):
                values = []
                title_is = True
                for key, value in xml_to_dict.items():
                    # 날짜 포맷 처리
                    
                    if key == "title" : 
                        if value is None:
                            title_is = False
                            break

                    if key == "appl_no":
                        if value is None or value == "":
                            title_is = False
                            break

                    if key == "abstract" and value is not None:
                        value = value.replace("\\", "")

                    value = self.value_fillter(value)
                    
                    values.append(value)

                if title_is :
                    # break
                    # pass
                    value_tuple = f"({', '.join(values)})"
                    if j == self.chunk_size - 1 or (i + j + 1) == len(self.xml_to_dict_list):
                        chunk_data.append(f"{value_tuple}\n")
                        chunk_data.append(self.__get_upsert_info())
                    else:
                        chunk_data.append(f"{value_tuple},\n")
                
            chunked_data.append("".join(chunk_data))
        
        return chunked_data

    def get_chunked_sub_table_sql_files(self):
        if self.service_type in ['design', 'trademark']:
            self.xml_to_dict_converter.mapper = KiprisPriorityXmlMapper()
        else:
            self.xml_to_dict_converter.mapper = KiprisIpcXmlMapper()


        mysql = Mysql()
        ipr_seq_dict = mysql.get_sub_table(self.table_name)

        colums = self.__get_mapper_dict() # ipc_cpc, ipc_cpc_code, ipr_seq
        insert_info = f"{self.__get_sub_insert_info()}\n"
        chunked_data = []
        # print(self.sub_dict_list)
        for i in range(0, len(self.sub_dict_list), self.chunk_size):
            
            chunk_data = [insert_info]
            for j, sub_xml_to_dict in enumerate(self.sub_dict_list[i:i + self.chunk_size]):
                # print(sub_xml_to_dict)
                
                values = []

                for c in colums:
                    value = None
                    if c in sub_xml_to_dict:
                        value = sub_xml_to_dict[c]

                    value = self.value_fillter(value)

                    if c == 'ipr_seq':
                        ipr_seq_key = str(sub_xml_to_dict['appl_no']) + str(sub_xml_to_dict['applicant_id']) + sub_xml_to_dict['serial_no']
                        value = str(ipr_seq_dict.get(ipr_seq_key))

                        if value is None:
                            break
                    values.append(value)

                value_tuple = f"({', '.join(values)})"
                if j == self.chunk_size - 1 or (i + j + 1) == len(self.xml_to_dict_list):
                        print("inin")
                        chunk_data.append(f"{value_tuple}\n")
                        chunk_data.append(self.__get_upsert_sub_info())
                else:
                    chunk_data.append(f"{value_tuple},\n")
                    
            chunked_data.append("".join(chunk_data))
        return chunked_data

    def save_file(self, filename: str, directory: str = "./"):
        # 경로가 존재하지 않으면 생성
        os.makedirs(directory, exist_ok=True)
        
        # 청크별 SQL 파일 저장
        chunked_sql_files = self.get_chunked_sql_files()

        for idx, sql_content in enumerate(chunked_sql_files, start=1):
            filepath = os.path.join(directory, f"{filename}_{idx}.sql")
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(sql_content)
            print(f"Saved {filepath}")

    def subtable_save_file(self, filename: str, directory: str = "./"):
        # 경로가 존재하지 않으면 생성
        os.makedirs(directory, exist_ok=True)
        # 청크별 SQL 파일 저장
        chunked_sql_files = self.get_chunked_sub_table_sql_files()
        for idx, sql_content in enumerate(chunked_sql_files, start=1):
            filepath = os.path.join(directory, f"{filename}_{idx}.sql")
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write("\n".join(sql_content))
            print(f"Saved {filepath}")
