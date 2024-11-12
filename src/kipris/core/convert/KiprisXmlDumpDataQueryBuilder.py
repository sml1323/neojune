import os
from datetime import datetime
from .KiprisDataCartridge import KiprisDataCartridge
from .KiprisXmlToDictConverter import KiprisXmlToDictConverter

class KiprisXmlDumpDataQueryBuilder():
    def __init__(
        self, 
        table_name:str="table_name", 
        xml_filename:str="xml_filename",
        xml_to_dict_converter_class:type[KiprisXmlToDictConverter] = KiprisXmlToDictConverter
    ):
        self.data = []
        self.table_name = table_name
        self.xml_to_dict_converter:KiprisXmlToDictConverter = xml_to_dict_converter_class(xml_filename=xml_filename)
        self.xml_to_dict_list = self.xml_to_dict_converter.parse()


    def __get_mapper_dict(self):
        return self.xml_to_dict_converter.mapper.get_dict_with_properties()
    
    def __get_insert_info(self):
        columns = ", ".join(self.__get_mapper_dict())
        return f"INSERT INTO {self.table_name} ({columns})"

    def append(self, data:KiprisDataCartridge):
        self.data.append(tuple(data.get_dict_with_properties().values()))

    def get_sql_file(self):
        self.data.append(f'{self.__get_insert_info()}\n')
        self.data.append("VALUES\n")
        
        for i, xml_to_dict in enumerate(self.xml_to_dict_list):
            values = []
            
            for value in xml_to_dict.values():
                if isinstance(value, str) and len(value) == 8 and value.isdigit():
                    try:
                        value = datetime.strptime(value, '%Y%m%d').strftime("'%Y-%m-%d'")
                    except ValueError:
                        pass
                elif value is None:
                    value = 'NULL'
                elif isinstance(value, str):
                    value = f"'{value}'"
                else:
                    value = str(value)  # 문자열이 아닌 값을 문자열로 변환
                
                values.append(value)
            
            value_tuple = f"({', '.join(values)})"  # 모든 값이 문자열로 변환됨
            if i == len(self.xml_to_dict_list) - 1:
                self.data.append(f"{value_tuple};\n")
            else:
                self.data.append(f"{value_tuple},\n")
                
        return "".join(self.data)
    

    def save_file(self, filename: str, directory: str = "./"):
        # 경로가 존재하지 않으면 생성
        os.makedirs(directory, exist_ok=True)
        
        # 파일 전체 경로
        filepath = os.path.join(directory, f"{filename}.sql")
        
        # SQL 내용 가져와서 저장
        sql_content = self.get_sql_file()
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(sql_content)