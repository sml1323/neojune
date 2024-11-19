from ..kipris.core.convert.KiprisXmlDumpDataQueryBuilder import KiprisXmlDumpDataQueryBuilder

from ..kipris.convert.converter.KiprisDesignXmlToDictConverter import KiprisDesignXmlToDictConverter
from ..kipris.convert.converter.KiprisPatentXmlToDictConverter import KiprisPatentXmlToDictConverter
from ..kipris.convert.converter.KiprisTrademarkXmlToDictConverter import KiprisTrademarkXmlToDictConverter

from ..util import util
from ..enum.Config import Config



### 기본 경로 
base_path = f"{Config.OUTPUT_PATH.value}/{util.get_timestamp()}/xml"
basic_save_path = f"{Config.OUTPUT_PATH.value}/{util.get_timestamp()}/sql"

# base_path = f"res/output/20241114/xml"
# basic_save_path = f"./res/output/20241114/sql"

# 기업
company_path = f"{base_path}/company"
company_save_path = f"{basic_save_path}/company"

design_xml_filename = f'{company_path}/design.xml'  # XML 파일 경로
patent_xml_filename = f'{company_path}/patent.xml'  # XML 파일 경로
trademark_xml_filename = f'{company_path}/trademark.xml'  # XML 파일 경로

# 대학    

university_path = f"{base_path}/university"
university_save_path = f"{basic_save_path}/university"

design_xml_filename = f'{university_path}/design.xml'  # XML 파일 경로
patent_xml_filename = f'{university_path}/patent.xml'  # XML 파일 경로
trademark_xml_filename = f'{university_path}/trademark.xml'  # XML 파일 경로



def run_company_design():
    company_design = KiprisXmlDumpDataQueryBuilder(
        table_name="TB24_company_design", 
        xml_filename=design_xml_filename,
        xml_to_dict_converter_class=KiprisDesignXmlToDictConverter
    )
    company_design.subtable_save_file('priority_design', f"{company_save_path}/priority")

def run_company_patent():
    company_patent = KiprisXmlDumpDataQueryBuilder(
        table_name="TB24_company_patent", 
        xml_filename=patent_xml_filename,
        xml_to_dict_converter_class=KiprisPatentXmlToDictConverter
    )
    company_patent.subtable_save_file('ipc_cpc', f"{company_save_path}/ipc_cpc")

def run_company_trademark():
    company_trademark = KiprisXmlDumpDataQueryBuilder(
        table_name="TB24_company_trademark", 
        xml_filename=trademark_xml_filename,
        xml_to_dict_converter_class=KiprisTrademarkXmlToDictConverter
    )
    company_trademark.subtable_save_file('priority_trademark', f"{company_save_path}/priority")
    


def run_university_design():
    university_design = KiprisXmlDumpDataQueryBuilder(
        table_name="TB24_university_design", 
        xml_filename=design_xml_filename,
        xml_to_dict_converter_class=KiprisDesignXmlToDictConverter
    )
    university_design.subtable_save_file('priority_design', f"{university_save_path}/priority")

def run_university_patent():
    university_patent = KiprisXmlDumpDataQueryBuilder(
        table_name="TB24_university_patent", 
        xml_filename=patent_xml_filename,
        xml_to_dict_converter_class=KiprisPatentXmlToDictConverter
    )
    university_patent.subtable_save_file('ipc_cpc', f"{university_save_path}/ipc_cpc")

def run_university_trademark():
    university_trademark = KiprisXmlDumpDataQueryBuilder(
        table_name="TB24_university_trademark", 
        xml_filename=trademark_xml_filename,
        xml_to_dict_converter_class=KiprisTrademarkXmlToDictConverter
    )
    university_trademark.subtable_save_file('priority_trademark', f"{university_save_path}/priority")



def main():
    run_company_design()
    run_company_patent()
    run_company_trademark()
    run_university_design()
    run_university_patent()
    run_university_trademark()
    pass
