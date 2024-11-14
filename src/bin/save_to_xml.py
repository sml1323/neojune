import asyncio
from ..db.mysql import Mysql
from ..kipris.process.xml_file_generator.KiprisPatentXmlFileGenerator import KiprisPatentXmlFileGenerator
from ..kipris.process.xml_file_generator.KiprisDesignXmlFileGenerator import KiprisDesignXmlFileGenerator
from ..kipris.process.xml_file_generator.KiprisTrademarkXmlFileGenerator import KiprisTrademarkXmlFileGenerator
from ..kipris.core.prosess.enum import KiprisXmlFileGeneratorEntityType
from ..util import monitoring

mysql = Mysql()


# company_logger = monitoring.setup_logger("company")
# company_logger.debug("TB24_200")
# university_logger = monitoring.setup_logger("university")
# university_logger.debug("TB24_210")


company_dir_path = "xml/company"
university_dir_path = "xml/university"
company_applicant_numbers = [[120140558200, 1]]
university_applicant_numbers = [[120010134557, 1]]
# mysql.get_all_company_no_id()
# mysql.get_all_university_no_id()


async def company_patent():
    await KiprisPatentXmlFileGenerator(
        "patent",company_dir_path, 
        company_applicant_numbers,
        KiprisXmlFileGeneratorEntityType.COMPANY
    ).save()

async def company_design():
    await KiprisDesignXmlFileGenerator(
        "design",company_dir_path, 
        company_applicant_numbers,
        KiprisXmlFileGeneratorEntityType.COMPANY
    ).save()

async def company_trademark():
    await KiprisTrademarkXmlFileGenerator(
        "trademark",company_dir_path, 
        company_applicant_numbers,
        KiprisXmlFileGeneratorEntityType.COMPANY
    ).save()


async def university_patent():
    await KiprisPatentXmlFileGenerator(
        "patent",university_dir_path, 
        university_applicant_numbers,
        KiprisXmlFileGeneratorEntityType.UNIVERSITY
    ).save()

async def university_design():
    await KiprisDesignXmlFileGenerator(
        "design",university_dir_path, 
        university_applicant_numbers,
        KiprisXmlFileGeneratorEntityType.UNIVERSITY
    ).save()

async def university_trademark():
    await KiprisTrademarkXmlFileGenerator(
        "trademark",university_dir_path, 
        university_applicant_numbers,
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
