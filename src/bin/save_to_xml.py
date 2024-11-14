import asyncio
from enum import Enum
from ..db.mysql import Mysql
from ..kipris.process.xml_file_generator.KiprisPatentXmlFileGenerator import KiprisPatentXmlFileGenerator
from ..kipris.process.xml_file_generator.KiprisDesignXmlFileGenerator import KiprisDesignXmlFileGenerator
from ..kipris.process.xml_file_generator.KiprisTrademarkXmlFileGenerator import KiprisTrademarkXmlFileGenerator
from ..kipris.core.prosess.enum import KiprisXmlFileGeneratorEntityType
from ..util import monitoring

class TableName(Enum):
    TB24_200 = "TB24_200"
    TB24_210 = "TB24_210"

class ApiType(Enum):
    PATENT = "patent"
    DESIGN = "design"
    TRADEMARK = "trademark"

def monitering(table_name:TableName, entity_type:KiprisXmlFileGeneratorEntityType, api_type:ApiType):
    logger = monitoring.setup_logger(f'{entity_type.value}: {api_type.value}')
    logger.debug(table_name.value)

mysql = Mysql()
COMPANY_DIR_PATH = f"xml/{KiprisXmlFileGeneratorEntityType.COMPANY.value}"
UNIVERSITY_DIR_PATH = f"xml/{KiprisXmlFileGeneratorEntityType.UNIVERSITY.value}"
COMPANY_APPLICANT_NUMBERS = [[120140558200, 1]]
UNIVERSITY_APPLICANT_NUMBERS = [[120010134557, 1]]
# COMPANY_APPLICANT_NUMBERS = mysql.get_all_company_no_id()
# UNIVERSITY_APPLICANT_NUMBERS = mysql.get_all_university_no_id()


async def company_patent():
    monitering(TableName.TB24_200, KiprisXmlFileGeneratorEntityType.COMPANY, ApiType.PATENT)
    await KiprisPatentXmlFileGenerator(
        ApiType.PATENT.value,
        COMPANY_DIR_PATH,
        COMPANY_APPLICANT_NUMBERS,
        KiprisXmlFileGeneratorEntityType.COMPANY
    ).save()

async def company_design():
    monitering(TableName.TB24_200, KiprisXmlFileGeneratorEntityType.COMPANY, ApiType.DESIGN)
    await KiprisDesignXmlFileGenerator(
        ApiType.DESIGN.value,
        COMPANY_DIR_PATH,
        COMPANY_APPLICANT_NUMBERS,
        KiprisXmlFileGeneratorEntityType.COMPANY
    ).save()

async def company_trademark():
    monitering(TableName.TB24_200, KiprisXmlFileGeneratorEntityType.COMPANY, ApiType.TRADEMARK)
    await KiprisTrademarkXmlFileGenerator(
        ApiType.TRADEMARK.value,
        COMPANY_DIR_PATH,
        COMPANY_APPLICANT_NUMBERS,
        KiprisXmlFileGeneratorEntityType.COMPANY
    ).save()


async def university_patent():
    monitering(TableName.TB24_210, KiprisXmlFileGeneratorEntityType.UNIVERSITY, ApiType.PATENT)
    await KiprisPatentXmlFileGenerator(
        ApiType.PATENT.value,
        UNIVERSITY_DIR_PATH,
        UNIVERSITY_APPLICANT_NUMBERS,
        KiprisXmlFileGeneratorEntityType.UNIVERSITY
    ).save()

async def university_design():
    monitering(TableName.TB24_210, KiprisXmlFileGeneratorEntityType.UNIVERSITY, ApiType.DESIGN)
    await KiprisDesignXmlFileGenerator(
        ApiType.DESIGN.value,
        UNIVERSITY_DIR_PATH,
        UNIVERSITY_APPLICANT_NUMBERS,
        KiprisXmlFileGeneratorEntityType.UNIVERSITY
    ).save()

async def university_trademark():
    monitering(TableName.TB24_210, KiprisXmlFileGeneratorEntityType.UNIVERSITY, ApiType.TRADEMARK)
    await KiprisTrademarkXmlFileGenerator(
        ApiType.TRADEMARK.value,
        UNIVERSITY_DIR_PATH,
        UNIVERSITY_APPLICANT_NUMBERS,
        KiprisXmlFileGeneratorEntityType.UNIVERSITY
    ).save()


async def main():
    await company_patent()
    await company_design()
    await company_trademark()
    await university_patent()
    await university_design()
    await university_trademark()



if __name__ == '__main__':
    asyncio.run(main())
