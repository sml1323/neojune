import time, asyncio, aiohttp
import xml.etree.ElementTree as ET
from .api_modules import design_api, patent_api, trademark_api
from ..db.mysql import Mysql
from .XMLEditor import XMLEditor


mysql = Mysql()


def get_app_no():
    return mysql.fetch_data_from_db('TB24_200',['app_no'], 1)[0][0]

def get_applicant_id():
    return mysql.fetch_data_from_db('TB24_200',['applicant_id'], 1)[0][0]

async def get_fetch_app_info(app_no, callback) -> list[str]:
    semaphore = asyncio.Semaphore(50)
    async with aiohttp.ClientSession() as session:
        async with semaphore:
            return await callback(app_no, session)
    

async def get_run_time(callback:callable, msg:str):
    start_time = time.time()
    await callback()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"총 걸린 시간 : {elapsed_time:.2f}초")
    print(msg)

async def main():
    patent, design, trademark = None, None, None
    app_no = get_app_no()
    applicant_id = get_applicant_id()

    async def get_info():
        nonlocal patent, design, trademark  # 바깥 스코프 변수에 접근
        patent = await get_fetch_app_info(app_no, patent_api.get_patent_info)
        design = await get_fetch_app_info(app_no, design_api.get_design_info)
        trademark = await get_fetch_app_info(app_no, trademark_api.get_trademark_info)
    await get_run_time(get_info , f"전체 호출 완료: 3개 신청자 처리")

    async def save_xml():
        xml_editor = XMLEditor()
        xml_editor.save_data_as_xml(applicant_id, patent, f"patent_data")
        xml_editor.save_data_as_xml(applicant_id, design, f"design_data")
        xml_editor.save_data_as_xml(applicant_id, trademark, f"trademark_data")
    await get_run_time(save_xml , "patent_data 저장 완료")

if __name__ == '__main__':
    asyncio.run(main())
