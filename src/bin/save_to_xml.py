import asyncio
from ..enum.KiprisEntityType import KiprisEntityType
from ..enum.ApiType import ApiType
from ..enum.TableName import TableName
from ..db.mysql import Mysql
from ..kipris.process.xml_file_generator.KiprisPatentXmlFileGenerator import KiprisPatentXmlFileGenerator
from ..kipris.process.xml_file_generator.KiprisDesignXmlFileGenerator import KiprisDesignXmlFileGenerator
from ..kipris.process.xml_file_generator.KiprisTrademarkXmlFileGenerator import KiprisTrademarkXmlFileGenerator
from ..enum.KiprisEntityType import KiprisEntityType
from ..util import monitoring


mysql = Mysql()

# 회사 데이터 저장 경로
COMPANY_DIR_PATH = f"xml/{KiprisEntityType.COMPANY.value}"
# 대학 데이터 저장 경로
UNIVERSITY_DIR_PATH = f"xml/{KiprisEntityType.UNIVERSITY.value}"

# 실제 데이터를 가져오려면 아래 주석을 해제하고 위의 테스트 데이터를 주석 처리합니다.
# COMPANY_APPLICANT_NUMBERS = mysql.get_all_company_no_id()
# UNIVERSITY_APPLICANT_NUMBERS = mysql.get_all_university_no_id()

# 테스트 데이터
COMPANY_APPLICANT_NUMBERS = mysql.get_limit_company_no_id(limit=100) 
UNIVERSITY_APPLICANT_NUMBERS = mysql.get_limit_company_no_id(limit=100) 

async def run_company_patent():
    monitoring.setup_bin_logger(TableName.TB24_200, KiprisEntityType.COMPANY, ApiType.PATENT)
    await KiprisPatentXmlFileGenerator(
        ApiType.PATENT.value,
        COMPANY_DIR_PATH,
        COMPANY_APPLICANT_NUMBERS,
        KiprisEntityType.COMPANY
    ).save()

async def run_company_design():
    monitoring.setup_bin_logger(TableName.TB24_200, KiprisEntityType.COMPANY, ApiType.DESIGN)
    await KiprisDesignXmlFileGenerator(
        ApiType.DESIGN.value,
        COMPANY_DIR_PATH,
        COMPANY_APPLICANT_NUMBERS,
        KiprisEntityType.COMPANY
    ).save()

async def run_company_trademark():
    monitoring.setup_bin_logger(TableName.TB24_200, KiprisEntityType.COMPANY, ApiType.TRADEMARK)
    await KiprisTrademarkXmlFileGenerator(
        ApiType.TRADEMARK.value,
        COMPANY_DIR_PATH,
        COMPANY_APPLICANT_NUMBERS,
        KiprisEntityType.COMPANY
    ).save()


async def run_university_patent():
    monitoring.setup_bin_logger(TableName.TB24_210, KiprisEntityType.UNIVERSITY, ApiType.PATENT)
    await KiprisPatentXmlFileGenerator(
        ApiType.PATENT.value,
        UNIVERSITY_DIR_PATH,
        UNIVERSITY_APPLICANT_NUMBERS,
        KiprisEntityType.UNIVERSITY
    ).save()

async def run_university_design():
    monitoring.setup_bin_logger(TableName.TB24_210, KiprisEntityType.UNIVERSITY, ApiType.DESIGN)
    await KiprisDesignXmlFileGenerator(
        ApiType.DESIGN.value,
        UNIVERSITY_DIR_PATH,
        UNIVERSITY_APPLICANT_NUMBERS,
        KiprisEntityType.UNIVERSITY
    ).save()

async def run_university_trademark():
    monitoring.setup_bin_logger(TableName.TB24_210, KiprisEntityType.UNIVERSITY, ApiType.TRADEMARK)
    await KiprisTrademarkXmlFileGenerator(
        ApiType.TRADEMARK.value,
        UNIVERSITY_DIR_PATH,
        UNIVERSITY_APPLICANT_NUMBERS,
        KiprisEntityType.UNIVERSITY
    ).save()


async def main():
    await run_company_patent()
    await run_company_design()
    await run_company_trademark()
    await run_university_patent()
    await run_university_design()
    await run_university_trademark()



if __name__ == '__main__':
    asyncio.run(main())
