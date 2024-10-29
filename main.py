import asyncio
import aiohttp
from api_modules import design_api, patent_api, trademark_api
import os
from dotenv import load_dotenv
import time
import MySQLdb
from datetime import datetime
from crud import connection, db_crud
import json


async def fetch_all_info(service_key, app_no, applicant_id, session, semaphore, pa_dict, de_dict, tr_dict):
    async with semaphore:
        tasks = [
            asyncio.create_task(patent_api.get_patent_info(service_key, app_no, session)),
            asyncio.create_task(design_api.get_design_info(service_key, app_no, session)),
            asyncio.create_task(trademark_api.get_trademark_info(service_key, app_no, session)),
        ]

        results = await asyncio.gather(*tasks)

        # data 부분만 추출하여 딕셔너리에 저장
        pa_dict[applicant_id] = {app_no: results[0]}
        de_dict[applicant_id] = {app_no: results[1]}
        tr_dict[applicant_id] = {app_no: results[2]}

        print(f"{app_no} 총 데이터 수 : {len(pa_dict) +len(de_dict) + len(tr_dict) }")

async def main():
    load_dotenv()
    service_key = os.getenv('SERVICE_KEY')
    semaphore = asyncio.Semaphore(30)
    limit = 5
    test_apps = db_crud.fetch_data_from_db('TB24_200',['app_no', 'applicant_id'],limit)

    
    start_time = time.time()

    pa_dict, de_dict, tr_dict = {}, {}, {}

    async with aiohttp.ClientSession() as session:
        tasks = []
        for app_no, applicant_id in test_apps:
            task = asyncio.create_task(fetch_all_info(service_key, app_no, applicant_id, session, semaphore, pa_dict, de_dict, tr_dict))
            tasks.append(task)
        await asyncio.gather(*tasks)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"전체 호출 완료: {len(test_apps)}개 신청자 처리, 총 걸린 시간 : {elapsed_time:.2f}초")


    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    start = time.time()
    with open(f"./save_to_json/patent_{timestamp}.json", "w") as pa_file, \
         open(f"./save_to_json/design_{timestamp}.json", "w") as de_file, \
         open(f"./save_to_json/trademark_{timestamp}.json", "w") as tr_file:
        json.dump(pa_dict, pa_file, ensure_ascii=False, indent=4)
        json.dump(de_dict, de_file, ensure_ascii=False, indent=4)
        json.dump(tr_dict, tr_file, ensure_ascii=False, indent=4)

    print("모든 데이터를 JSON 파일로 저장 완료")
    end = time.time()
    elapsed_time = end - start
    print(f"걸린 시간: {elapsed_time}")
if __name__ == '__main__':
    asyncio.run(main())
