import time, asyncio, aiohttp
import xml.etree.ElementTree as ET
from ..db.mysql import Mysql
from .api_modules import design_api, patent_api, trademark_api
from .kipris_xml.KiprisXmlData import KiprisXmlData
from .Kipris.core.KiprisXMLParserCore import KiprisXMLParser
from .kipris_xml.KiprisFetchData import KiprisFetchData
from .kipris_xml.KiprisXmlDataGenerator import KiprisXmlDataGenerator
from .Kipris.KiprisApplicantInfoFetcher import KiprisApplicantInfoFetcher
from .Kipris.core.KiprisParams import KiprisParams
from .Kipris.params.PatentParams import PatentParams
from .Kipris.KiprisFetcher import KiprisFetcher
mysql = Mysql()


def get_app_no():
    return mysql.fetch_data_from_db('TB24_200',['app_no'], 1)[0][0]

def get_applicant_id():
    return mysql.fetch_data_from_db('TB24_200',['applicant_id'], 1)[0][0]



async def get_fetch_app_info(app_no, callback) -> KiprisFetchData:
    async with aiohttp.ClientSession() as session:
        data = await callback(app_no, session)
        return KiprisFetchData(app_no, data)





async def get_fetch_app_infos(url, params: list[KiprisParams]) -> list[KiprisFetchData]:
    semaphore = asyncio.Semaphore(50)

    async def task(url, param:KiprisParams):
        async with semaphore:
            info = KiprisApplicantInfoFetcher(url, param)
            return await info.get_info()

    tasks = []
    # params[0].get_dict()
    for param in params:
        tasks.append(asyncio.create_task(task(url, param)))
    print(tasks)
    return await asyncio.gather(*tasks)


async def get_run_time(callback:callable, msg:str):
    start_time = time.time()
    await callback()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"총 걸린 시간 : {elapsed_time:.2f}초")
    print(msg)


async def main():
    params, design, trademark = None, None, None
    app_no = get_app_no()
    applicant_id = get_applicant_id()
    # kipris_xml_parser = KiprisXMLParser()
    # print(app_no, applicant_id)
    
    async def get_info():
        nonlocal params, design, trademark  # 바깥 스코프 변수에 접근
        applicant_numbers = [
            120080091393, # p3
            # 120070509242 # p23

            # 120090600987,
            # 120090148165,
            # 120090359981, 
            # 120090359981, 
            # 120100466769, 
            # 120090148165
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
        # patent = await get_fetch_app_infos(app_nos, kipris_xml_parser.get_info)
        # patent = await get_fetch_app_infos(app_nos, patent_api.get_patent_info)

        # kipris_applicant_info_fetcher = KiprisApplicantInfoFetcher(url, params)
        # patent = await kipris_applicant_info_fetcher.get_info()
        
        url = "http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/applicantNameSearchInfo"
        patent_params = [
            # PatentParams(120010134557),
            PatentParams(120010134557),
            PatentParams(120080091393), # p3
            # PatentParams(120070509242), # p23
            # PatentParams(120080034715),
            # PatentParams(120080176296),
        ]

        kipris_fetcher = KiprisFetcher(url, patent_params)
        params = await kipris_fetcher.get_fetch_app_infos()
        # patent = await get_fetch_app_infos(app_nos, patent_api.get_patent_info)
        # design = await get_fetch_app_infos(app_nos, design_api.get_design_info)
        # trademark = await get_fetch_app_infos(app_nos, trademark_api.get_trademark_info)
        # print(patent[0].data)
    
    # await get_run_time(get_info , f"전체 호출 완료: 3개 신청자 처리")
    # print(patent)
    
    

    async def save_xml():
        # kipris_xml = KiprisXmlData(KiprisFetchData("123", "data"))
        # kipris_xml = KiprisXmlData(patent[0])
        # kipris_xml.apply()
        # kipris_xml.save("patent_data")
        kipris_xml_dataGenerator = KiprisXmlDataGenerator(params)
        kipris_xml_dataGenerator.apply()
        kipris_xml_dataGenerator.save("patent")

        # kipris_xml_dataGenerator.append_data_lists(design)
        # kipris_xml_dataGenerator.apply()
        # kipris_xml_dataGenerator.save("design")

        # kipris_xml_dataGenerator.append_data_lists(trademark)
        # kipris_xml_dataGenerator.apply()
        # kipris_xml_dataGenerator.save("trademark")

        # xml_applican_id_registor.save("design_data", design)
        # xml_applican_id_registor.save("trademark_data", trademark)
    # await get_run_time(save_xml , "patent_data 저장 완료")




if __name__ == '__main__':
    asyncio.run(main())
