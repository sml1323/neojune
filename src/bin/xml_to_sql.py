from enum import Enum
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

class ApiType(Enum):
    PATENT = "patent"
    DESIGN = "design"
    TRADEMARK = "trademark"


BASE_PATH = f"src/test/kipris/convert/xml"
BASIC_SAVE_PATH = f"./res/output/{util.get_timestamp()}/sql"
COMPANY_PATH = f"{BASIC_SAVE_PATH}/company"
UNIVERSITY_PATH = f"{BASIC_SAVE_PATH}/university"



def run_company_design():
    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.COMPANY_PATENT.value, 
        xml_filename=f'{BASE_PATH}/{ApiType.DESIGN.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisDesignXmlToDictConverter
    )
    query_builder.save_file(ApiType.DESIGN.value, COMPANY_PATH)

def run_company_patent():
    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.COMPANY_DESIGN.value, 
        xml_filename=f'{BASE_PATH}/{ApiType.PATENT.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisPatentXmlToDictConverter
    )
    query_builder.save_file(ApiType.PATENT.value, COMPANY_PATH)

def run_company_trademark():
    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.COMPANY_TRADEMARK.value, 
        xml_filename=f'{BASE_PATH}/{ApiType.TRADEMARK.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisTrademarkXmlToDictConverter
    )
    query_builder.save_file(ApiType.TRADEMARK.value, COMPANY_PATH)


def run_university_design():
    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.UNIVERSITY_PATENT.value, 
        xml_filename=f'{BASE_PATH}/{ApiType.DESIGN.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisDesignXmlToDictConverter
    )
    query_builder.save_file(ApiType.DESIGN.value, UNIVERSITY_PATH)

def run_university_patent():
    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.UNIVERSITY_DESIGN.value, 
        xml_filename=f'{BASE_PATH}/{ApiType.PATENT.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisPatentXmlToDictConverter
    )
    query_builder.save_file(ApiType.PATENT.value, UNIVERSITY_PATH)

def run_university_trademark():
    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.UNIVERSITY_TRADEMARK.value, 
        xml_filename=f'{BASE_PATH}/{ApiType.TRADEMARK.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisTrademarkXmlToDictConverter
    )
    query_builder.save_file(ApiType.TRADEMARK.value, UNIVERSITY_PATH)



def main():
    run_company_design()
    run_company_patent()
    run_company_trademark()
    run_university_design()
    run_university_patent()
    run_university_trademark()
    pass
