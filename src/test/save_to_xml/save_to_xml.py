import asyncio
from ...db.mysql import Mysql
from ...kipris.parsing.xml.KiprisXmlDataGenerator import KiprisXmlDataGenerator
from ...kipris.parsing.fetcher.KiprisPatentFetcher import KiprisPatentFetcher
from ...kipris.parsing.fetcher.KiprisDesignFetcher import KiprisDesignFetcher
from ...kipris.parsing.fetcher.KiprisTrademarkFetcher import KiprisTrademarkFetcher
from ...util import util
from ...util import monitoring
mysql = Mysql()



class Info():
    def __init__(self):
        self.patent = None
        self.design = None
        self.trademark = None


async def main(table_name="TB24_200", dir_path="xml/company"):
    print(table_name)
    async def get_info() -> Info:
        info = Info()
        if table_name == "TB24_200":
            company_logger = monitoring.setup_logger("company")
            company_logger.debug("TB24_200")
            applicant_numbers = mysql.get_all_company_no_id()
            # applicant_numbers = mysql.get_limit_company_no_id(5)
            # p3: 120080091393,  p23: 120070509242
            # applicant_numbers = [[120070509242, 10],[120080091393, 20]]
            # applicant_numbers = [[120140558200, 1]]
        else:
            university_logger = monitoring.setup_logger("university")
            university_logger.debug("TB24_210")
            applicant_numbers = mysql.get_all_university_no_seq()
            # applicant_numbers = mysql.get_limit_university_no_seq(5)
            # applicant_numbers = [[220050095099, 1]]

        async def patent_action_api():
            patent_fetcher = KiprisPatentFetcher(applicant_numbers)
            return await patent_fetcher.get_infos("patent")
    
        async def design_action_api():
            design_fetcher = KiprisDesignFetcher(applicant_numbers)
            return await design_fetcher.get_infos("design")
    
        async def trademark_action_api():
            trademark_fetcher = KiprisTrademarkFetcher(applicant_numbers)
            return await trademark_fetcher.get_infos("trademark")
        
        info.patent = await util.execute_with_time_async("patent_action_api", patent_action_api)
        info.design = await util.execute_with_time_async("design_action_api", design_action_api)
        info.trademark = await util.execute_with_time_async("trademark_action_api", trademark_action_api)
        return info

    info:Info = await util.execute_with_time_async("`전체 호출 완료: 3개 신청자 처리", get_info)
    
    print("===========================================")

    async def save_xml(info:Info):
        kipris_xml_dataGenerator = KiprisXmlDataGenerator()
        async def action_patent():
            kipris_xml_dataGenerator.append_data_lists(info.patent)
            kipris_xml_dataGenerator.apply()
            kipris_xml_dataGenerator.save(f"patent", dir_path)
        
        async def action_design():
            kipris_xml_dataGenerator.append_data_lists(info.design)
            kipris_xml_dataGenerator.apply()
            kipris_xml_dataGenerator.save(f"design", dir_path)
        
        async def action_trademark():
            kipris_xml_dataGenerator.append_data_lists(info.trademark)
            kipris_xml_dataGenerator.apply()
            kipris_xml_dataGenerator.save(f"trademark", dir_path)

        await util.execute_with_time_async("### patent xml save", action_patent)
        await util.execute_with_time_async("### design xml save", action_design)
        await util.execute_with_time_async("### trademark xml save", action_trademark)


    await util.execute_with_time_async("xml 저장 완료", save_xml, info)

if __name__ == '__main__':
    asyncio.run(main())
