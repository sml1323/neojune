from ....kipris.core.convert.KiprisXmlDumpDataQueryBuilder import KiprisXmlDumpDataQueryBuilder

from ....kipris.convert.converter.KiprisDesignXmlToDictConverter import KiprisDesignXmlToDictConverter
from ....kipris.convert.converter.KiprisPatentXmlToDictConverter import KiprisPatentXmlToDictConverter
from ....kipris.convert.converter.KiprisTrademarkXmlToDictConverter import KiprisTrademarkXmlToDictConverter

from ....util import util



def main():

    ### 기본 경로 
    base_path = f"res/output/{util.get_timestamp()}/xml"
    basic_save_path = f"./res/output/{util.get_timestamp()}/sql"

    ##### 기업
    company_path = f"{base_path}/company"
    company_save_path = f"{basic_save_path}/company"

    design_xml_filename = f'{company_path}/design.xml'  # XML 파일 경로
    patent_xml_filename = f'{company_path}/patent.xml'  # XML 파일 경로
    trademark_xml_filename = f'{company_path}/trademark.xml'  # XML 파일 경로

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

    company_design.save_file("design", company_save_path)
    company_patent.save_file("patent", company_save_path)
    company_trademark.save_file("trademark", company_save_path)
    

    ## 대학    
    
    university_path = f"{base_path}/university"
    university_save_path = f"{basic_save_path}/university"

    design_xml_filename = f'{university_path}/design.xml'  # XML 파일 경로
    patent_xml_filename = f'{university_path}/patent.xml'  # XML 파일 경로
    trademark_xml_filename = f'{university_path}/trademark.xml'  # XML 파일 경로
    
    university_design = KiprisXmlDumpDataQueryBuilder(
        table_name="TB24_university_design", 
        xml_filename=design_xml_filename,
        xml_to_dict_converter_class=KiprisDesignXmlToDictConverter
    )
    university_patent = KiprisXmlDumpDataQueryBuilder(
        table_name="TB24_university_patent", 
        xml_filename=patent_xml_filename,
        xml_to_dict_converter_class=KiprisPatentXmlToDictConverter
    )
    university_trademark = KiprisXmlDumpDataQueryBuilder(
        table_name="TB24_university_trademark", 
        xml_filename=trademark_xml_filename,
        xml_to_dict_converter_class=KiprisTrademarkXmlToDictConverter
    )

    
    university_design.save_file("design", university_save_path)
    university_patent.save_file("patent", university_save_path)
    university_trademark.save_file("trademark", university_save_path)


    # print(sql)
    pass