from ....kipris.core.convert.KiprisXmlDumpDataQueryBuilder import KiprisXmlDumpDataQueryBuilder

from ....kipris.convert.converter.KiprisDesignXmlToDictConverter import KiprisDesignXmlToDictConverter
from ....kipris.convert.converter.KiprisPatentXmlToDictConverter import KiprisPatentXmlToDictConverter
from ....kipris.convert.converter.KiprisTrademarkXmlToDictConverter import KiprisTrademarkXmlToDictConverter

from ....util import util



def main():
    base_path = f"src/test/kipris/convert/xml"
    basic_save_path = f"./res/output/{util.get_timestamp()}/sql"
    company_path = f"{basic_save_path}/company"
    university_path = f"{basic_save_path}/university"

    design_xml_filename = f'{base_path}/design.xml'  # XML 파일 경로
    patent_xml_filename = f'{base_path}/patent.xml'  # XML 파일 경로
    trademark_xml_filename = f'{base_path}/trademark.xml'  # XML 파일 경로

    company_design = KiprisXmlDumpDataQueryBuilder(
        table_name="TB24_company_design", 
        xml_filename=design_xml_filename,
        xml_to_dict_converter_class=KiprisDesignXmlToDictConverter
    )
    company_patent = KiprisXmlDumpDataQueryBuilder(
        table_name="TB24_company_patent", 
        xml_filename=patent_xml_filename,
        xml_to_dict_converter_class=KiprisPatentXmlToDictConverter
    )
    company_trademark = KiprisXmlDumpDataQueryBuilder(
        table_name="TB24_company_trademark", 
        xml_filename=trademark_xml_filename,
        xml_to_dict_converter_class=KiprisTrademarkXmlToDictConverter
    )
    # design.append()
    # design.get_sql_file()
    
    company_design.save_file("design", company_path)
    company_patent.save_file("patent", company_path)
    company_trademark.save_file("trademark", company_path)


    # print(sql)
    pass