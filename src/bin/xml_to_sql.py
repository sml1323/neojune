from ..enum.KiprisEntityType import KiprisEntityType
from ..enum.ApiType import ApiType
from ..enum.TableName import TableName
from ..kipris.core.convert.KiprisXmlDumpDataQueryBuilder import KiprisXmlDumpDataQueryBuilder
from ..kipris.convert.converter.KiprisDesignXmlToDictConverter import KiprisDesignXmlToDictConverter
from ..kipris.convert.converter.KiprisPatentXmlToDictConverter import KiprisPatentXmlToDictConverter
from ..kipris.convert.converter.KiprisTrademarkXmlToDictConverter import KiprisTrademarkXmlToDictConverter

from ..util import util
from ..util import monitoring



# XML 파일들이 위치한 디렉토리
XML_DIR = "20241114" 

# XML 파일들의 기본 경로
XML_BASE_PATH = f"res/output/{XML_DIR}/xml" 

# 회사 관련 XML 파일 경로
COMPANY_XML_PATH = f"{XML_BASE_PATH}/{KiprisEntityType.COMPANY.value}" 

# 대학 관련 XML 파일 경로
UNIVERSITY_XML_PATH = f"{XML_BASE_PATH}/university" 


# SQL 파일들이 저장될 기본 경로 (타임스탬프 포함)
BASIC_SQL_PATH = f"./res/output/{util.get_timestamp()}/sql" 

# 회사 관련 SQL 파일 경로 (주의: KiprisEntityType.UNIVERSITY 사용)
COMPANY_SQL_PATH = f"{BASIC_SQL_PATH}/{KiprisEntityType.UNIVERSITY.value}" 

# 대학 관련 SQL 파일 경로
UNIVERSITY_SQL_PATH = f"{BASIC_SQL_PATH}/university" 


### company ###

def run_company_design():
    monitoring.setup_bin_logger(TableName.TB24_COMPANY_PATENT, KiprisEntityType.COMPANY, ApiType.DESIGN)

    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.TB24_COMPANY_PATENT.value, 
        xml_filename=f'{COMPANY_XML_PATH}/{ApiType.DESIGN.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisDesignXmlToDictConverter
    )
    query_builder.save_file(ApiType.DESIGN.value, COMPANY_SQL_PATH)

def run_company_patent():
    monitoring.setup_bin_logger(TableName.TB24_COMPANY_DESIGN, KiprisEntityType.COMPANY, ApiType.PATENT)

    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.TB24_COMPANY_DESIGN.value, 
        xml_filename=f'{COMPANY_XML_PATH}/{ApiType.PATENT.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisPatentXmlToDictConverter
    )
    query_builder.save_file(ApiType.PATENT.value, COMPANY_SQL_PATH)

def run_company_trademark():
    monitoring.setup_bin_logger(TableName.TB24_COMPANY_TRADEMARK, KiprisEntityType.COMPANY, ApiType.TRADEMARK)

    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.TB24_COMPANY_TRADEMARK.value, 
        xml_filename=f'{COMPANY_XML_PATH}/{ApiType.TRADEMARK.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisTrademarkXmlToDictConverter
    )
    query_builder.save_file(ApiType.TRADEMARK.value, COMPANY_SQL_PATH)


### university ###

def run_university_design():
    monitoring.setup_bin_logger(TableName.TB24_UNIVERSITY_DESIGN, KiprisEntityType.UNIVERSITY, ApiType.DESIGN)

    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.TB24_UNIVERSITY_DESIGN.value, 
        xml_filename=f'{UNIVERSITY_XML_PATH}/{ApiType.DESIGN.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisDesignXmlToDictConverter
    )
    query_builder.save_file(ApiType.DESIGN.value, UNIVERSITY_SQL_PATH)

def run_university_patent():
    monitoring.setup_bin_logger(TableName.TB24_UNIVERSITY_PATENT, KiprisEntityType.UNIVERSITY, ApiType.PATENT)

    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.TB24_UNIVERSITY_PATENT.value, 
        xml_filename=f'{UNIVERSITY_XML_PATH}/{ApiType.PATENT.value}.xml',  # XML 파일 경로
        xml_to_dict_converter_class=KiprisPatentXmlToDictConverter
    )
    query_builder.save_file(ApiType.PATENT.value, UNIVERSITY_SQL_PATH)

def run_university_trademark():
    monitoring.setup_bin_logger(TableName.TB24_UNIVERSITY_TRADEMARK, KiprisEntityType.UNIVERSITY, ApiType.TRADEMARK)
    query_builder = KiprisXmlDumpDataQueryBuilder(
        table_name=TableName.TB24_UNIVERSITY_TRADEMARK.value, 
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
