import time, asyncio
from ..db.mysql import Mysql
from .Kipris.xml.KiprisXmlDataGenerator import KiprisXmlDataGenerator

from .Kipris.fetcher.KiprisPatentFetcher import KiprisPatentFetcher
from .Kipris.fetcher.KiprisDesignFetcher import KiprisDesignFetcher
from .Kipris.fetcher.KiprisTrademarkFetcher import KiprisTrademarkFetcher
from .Kipris.params.KiprisDesignPrams import KiprisDesignPrams

mysql = Mysql()


async def get_run_time(callback:callable, msg:str):
    start_time = time.time()
    await callback()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"총 걸린 시간 : {elapsed_time:.2f}초")
    print(msg)


async def main():
    patent, design, trademark = None, None, None
    
    async def get_info():
        nonlocal patent, design, trademark  # 바깥 스코프 변수에 접근
        applicant_numbers = [
            # 120080091393, # p3
            # 120070509242 # p23

            120090600987,
            # 120090148165,
            # 120090359981, 
            # 120090359981, 
            # 120100466769, 
            # 120090148165,
            # 120010134557, 
            # 120010134557, 120010471074, 120040124445, 120060278426, 120070304548,
            # 120070304600, 120070332696, 120070355061, 120070461599, 120070485151,
            # 120070509242, 120070522700, 120070527120, 120080024434, 120080025101,
            # 120080034715, 120080063216, 120080091393, 120080103646, 120080126011,
            # 120080176296, 120080213024, 120080257391, 120080258905, 120080391823,
            # 120080414560, 120080416822, 120080548918, 120080580893, 120090001048,
            # 120090006334, 120090056151, 120090071148, 120090089460, 120090118306,
            # 120090124740, 120090144282, 120090283563, 120090380201, 120090380737,
            # 120090383748, 120090445711, 120090535974, 120090538661, 120090560865,
            # 120090600987, 120090605446, 120100010958, 120100136087, 120100136201,
            # 120100225203, 120100264556, 120100352749, 120100374784,
        ]

        _applicant_numbers = mysql.get_limit_app_no_and_applicant_id(100)
        
        patent_fetcher = KiprisPatentFetcher(_applicant_numbers)
        patent = await patent_fetcher.get_infos()

        design_fetcher = KiprisDesignFetcher(_applicant_numbers)
        design = await design_fetcher.get_infos()

        trademark_fetcher = KiprisTrademarkFetcher(_applicant_numbers)
        trademark = await trademark_fetcher.get_infos()

    await get_run_time(get_info , f"전체 호출 완료: 3개 신청자 처리")
    
    

    async def save_xml():
        kipris_xml_dataGenerator = KiprisXmlDataGenerator(patent)
        kipris_xml_dataGenerator.apply()
        kipris_xml_dataGenerator.save("patent")

        kipris_xml_dataGenerator.append_data_lists(design)
        kipris_xml_dataGenerator.apply()
        kipris_xml_dataGenerator.save("design")

        kipris_xml_dataGenerator.append_data_lists(trademark)
        kipris_xml_dataGenerator.apply()
        kipris_xml_dataGenerator.save("trademark")

    await get_run_time(save_xml , "patent_data 저장 완료")






if __name__ == '__main__':
    asyncio.run(main())
