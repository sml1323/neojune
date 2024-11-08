import asyncio
from ...db.mysql import Mysql
from ...kipris.parsing.xml.KiprisXmlDataGenerator import KiprisXmlDataGenerator
from ...kipris.parsing.fetcher.KiprisPatentFetcher import KiprisPatentFetcher
from ...kipris.parsing.fetcher.KiprisDesignFetcher import KiprisDesignFetcher
from ...kipris.parsing.fetcher.KiprisTrademarkFetcher import KiprisTrademarkFetcher
from ...util import util
import time

mysql = Mysql()


async def main(table_name):
    patent, design, trademark = None, None, None
    
    async def get_info():
        nonlocal patent, design, trademark  # 바깥 스코프 변수에 접근
        isuniv = table_name == 'TB24_210' # table name에 따라 True, False 리턴
        # _applicant_numbers = mysql.get_all_app_no_and_applicant_id(table_name)
        # p3: 120080091393,  p23: 120070509242
        # _applicant_numbers = [[120070509242, 10],[120080091393, 20]]
        _applicant_numbers = [[120140558200, 1]]
# 
        kipris_xml_dataGenerator = KiprisXmlDataGenerator()
        
        if True:
            async def patent_action_api():
                nonlocal patent
                patent_fetcher = KiprisPatentFetcher(_applicant_numbers)
                patent = await patent_fetcher.get_infos("patent 처리 시간")
            await util.get_run_time(patent_action_api, "patent_action_api")

            async def patent_action_save():
                kipris_xml_dataGenerator.append_data_lists(patent)
                kipris_xml_dataGenerator.apply()
                file = "univ_patent" if isuniv else "patent"
                kipris_xml_dataGenerator.save(file)
            await util.get_run_time(patent_action_save, "patent_action_save")
        
        if True:
            async def design_action_api():
                nonlocal design
                design_fetcher = KiprisDesignFetcher(_applicant_numbers)
                design = await design_fetcher.get_infos("design")
            await util.get_run_time(design_action_api, "design_action_api")

            async def design_action_save():
                
                kipris_xml_dataGenerator.append_data_lists(design)
                kipris_xml_dataGenerator.apply()
                file = "univ_design" if isuniv else "design"
                kipris_xml_dataGenerator.save(file)
            await util.get_run_time(design_action_save, "design_action_save")
        
        if True:
            async def trademark_action_api():
                nonlocal trademark

                trademark_fetcher = KiprisTrademarkFetcher(_applicant_numbers)
                trademark = await trademark_fetcher.get_infos("trademark")
            await util.get_run_time(trademark_action_api, "trademark_action_api")

            async def trademark_action_save():

                kipris_xml_dataGenerator.append_data_lists(trademark)
                kipris_xml_dataGenerator.apply()
                file = "univ_trademark" if isuniv else "trademark"
                kipris_xml_dataGenerator.save(file)
            await util.get_run_time(trademark_action_save, "trademark_action_save")

        

    await util.get_run_time(get_info , f"전체 호출 완료: 3개 신청자 처리")
    
    

    # async def save_xml():
    #     kipris_xml_dataGenerator = KiprisXmlDataGenerator(patent)
    #     # kipris_xml_dataGenerator = KiprisXmlDataGenerator(design)
    #     kipris_xml_dataGenerator.apply()
    #     kipris_xml_dataGenerator.save("patent")

    #     kipris_xml_dataGenerator.append_data_lists(design)
    #     kipris_xml_dataGenerator.apply()
    #     kipris_xml_dataGenerator.save("design")

    #     kipris_xml_dataGenerator.append_data_lists(trademark)
    #     kipris_xml_dataGenerator.apply()
    #     kipris_xml_dataGenerator.save("trademark")

    # await util.get_run_time(save_xml , "patent_data 저장 완료")






if __name__ == '__main__':
    asyncio.run(main())
