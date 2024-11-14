from enum import Enum
from ..enum.KiprisEntityType import KiprisEntityType
from ..enum.ApiType import ApiType
from ..kipris.core.convert.KiprisXmlDumpDataQueryBuilder import KiprisXmlDumpDataQueryBuilder
from ..kipris.convert.converter.KiprisDesignXmlToDictConverter import KiprisDesignXmlToDictConverter
from ..kipris.convert.converter.KiprisPatentXmlToDictConverter import KiprisPatentXmlToDictConverter
from ..kipris.convert.converter.KiprisTrademarkXmlToDictConverter import KiprisTrademarkXmlToDictConverter

from ..util import util

class TableName(Enum):
    COMPANY_PATENT = "TB24_company_patent"
    COMPANY_DESIGN = "TB24_company_design"
    COMPANY_TRADEMARK = "TB24_company_trademark"
    UNIVERSITY_PATENT = "TB24_university_patent"
    UNIVERSITY_DESIGN = "TB24_university_design"
    UNIVERSITY_TRADEMARK = "TB24_university_trademark"


XML_DIR = "20241114"
XML_BASE_PATH = f"res/output/{XML_DIR}/xml"
COMPANY_XML_PATH = f"{XML_BASE_PATH}/{KiprisEntityType.COMPANY.value}"
UNIVERSITY_XML_PATH = f"{XML_BASE_PATH}/university"

BASIC_SQL_PATH = f"./res/output/{util.get_timestamp()}/sql"
COMPANY_SQL_PATH = f"{BASIC_SQL_PATH}/{KiprisEntityType.UNIVERSITY.value}"
UNIVERSITY_SQL_PATH = f"{BASIC_SQL_PATH}/university"



def run_company_design():
    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.COMPANY_PATENT.value, 
        xml_filename=f'{COMPANY_XML_PATH}/{ApiType.DESIGN.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisDesignXmlToDictConverter
    )
    query_builder.save_file(ApiType.DESIGN.value, COMPANY_SQL_PATH)

def run_company_patent():
    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.COMPANY_DESIGN.value, 
        xml_filename=f'{COMPANY_XML_PATH}/{ApiType.PATENT.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisPatentXmlToDictConverter
    )
    query_builder.save_file(ApiType.PATENT.value, COMPANY_SQL_PATH)

def run_company_trademark():
    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.COMPANY_TRADEMARK.value, 
        xml_filename=f'{COMPANY_XML_PATH}/{ApiType.TRADEMARK.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisTrademarkXmlToDictConverter
    )
    query_builder.save_file(ApiType.TRADEMARK.value, COMPANY_SQL_PATH)


def run_university_design():
    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.UNIVERSITY_PATENT.value, 
        xml_filename=f'{UNIVERSITY_XML_PATH}/{ApiType.DESIGN.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisDesignXmlToDictConverter
    )
    query_builder.save_file(ApiType.DESIGN.value, UNIVERSITY_SQL_PATH)

def run_university_patent():
    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.UNIVERSITY_DESIGN.value, 
        xml_filename=f'{UNIVERSITY_XML_PATH}/{ApiType.PATENT.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisPatentXmlToDictConverter
    )
    query_builder.save_file(ApiType.PATENT.value, UNIVERSITY_SQL_PATH)

def run_university_trademark():
    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.UNIVERSITY_TRADEMARK.value, 
        xml_filename=f'{UNIVERSITY_XML_PATH}/{ApiType.TRADEMARK.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisTrademarkXmlToDictConverter
    )
    query_builder.save_file(ApiType.TRADEMARK.value, UNIVERSITY_SQL_PATH)



def main():
    run_company_design()
    run_company_patent()
    run_company_trademark()
    run_university_design()
    run_university_patent()
    run_university_trademark()
    pass
