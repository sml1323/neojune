import asyncio
from enum import Enum
from ..db.mysql import Mysql
from ..kipris.process.xml_file_generator.KiprisPatentXmlFileGenerator import KiprisPatentXmlFileGenerator
from ..kipris.process.xml_file_generator.KiprisDesignXmlFileGenerator import KiprisDesignXmlFileGenerator
from ..kipris.process.xml_file_generator.KiprisTrademarkXmlFileGenerator import KiprisTrademarkXmlFileGenerator
from ..enum.KiprisEntityType import KiprisEntityType
from ..util import monitoring

class TableName(Enum):
    TB24_200 = "TB24_200"
    TB24_210 = "TB24_210"

class ApiType(Enum):
    PATENT = "patent"
    DESIGN = "design"
    TRADEMARK = "trademark"

def monitering(table_name:TableName, entity_type:KiprisEntityType, api_type:ApiType):
    logger = monitoring.setup_logger(f'{entity_type.value}: {api_type.value}')
    logger.debug(table_name.value)

mysql = Mysql()
COMPANY_DIR_PATH = f"xml/{KiprisEntityType.COMPANY.value}"
UNIVERSITY_DIR_PATH = f"xml/{KiprisEntityType.UNIVERSITY.value}"
COMPANY_APPLICANT_NUMBERS = [[120140558200, 1]]
UNIVERSITY_APPLICANT_NUMBERS = [[120010134557, 1]]
# COMPANY_APPLICANT_NUMBERS = mysql.get_all_company_no_id()
# UNIVERSITY_APPLICANT_NUMBERS = mysql.get_all_university_no_id()


async def run_company_patent():
    monitering(TableName.TB24_200, KiprisEntityType.COMPANY, ApiType.PATENT)
    await KiprisPatentXmlFileGenerator(
        ApiType.PATENT.value,
        COMPANY_DIR_PATH,
        COMPANY_APPLICANT_NUMBERS,
        KiprisEntityType.COMPANY
    ).save()

async def run_company_design():
    monitering(TableName.TB24_200, KiprisEntityType.COMPANY, ApiType.DESIGN)
    await KiprisDesignXmlFileGenerator(
        ApiType.DESIGN.value,
        COMPANY_DIR_PATH,
        COMPANY_APPLICANT_NUMBERS,
        KiprisEntityType.COMPANY
    ).save()

async def run_company_trademark():
    monitering(TableName.TB24_200, KiprisEntityType.COMPANY, ApiType.TRADEMARK)
    await KiprisTrademarkXmlFileGenerator(
        ApiType.TRADEMARK.value,
        COMPANY_DIR_PATH,
        COMPANY_APPLICANT_NUMBERS,
        KiprisEntityType.COMPANY
    ).save()


async def run_university_patent():
    monitering(TableName.TB24_210, KiprisEntityType.UNIVERSITY, ApiType.PATENT)
    await KiprisPatentXmlFileGenerator(
        ApiType.PATENT.value,
        UNIVERSITY_DIR_PATH,
        UNIVERSITY_APPLICANT_NUMBERS,
        KiprisEntityType.UNIVERSITY
    ).save()

async def run_university_design():
    monitering(TableName.TB24_210, KiprisEntityType.UNIVERSITY, ApiType.DESIGN)
    await KiprisDesignXmlFileGenerator(
        ApiType.DESIGN.value,
        UNIVERSITY_DIR_PATH,
        UNIVERSITY_APPLICANT_NUMBERS,
        KiprisEntityType.UNIVERSITY
    ).save()

async def run_university_trademark():
    monitering(TableName.TB24_210, KiprisEntityType.UNIVERSITY, ApiType.TRADEMARK)
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
