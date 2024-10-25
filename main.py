import asyncio
import aiohttp
from api_modules import design_api, patent_api, trademark_api, biz_api
import os
from dotenv import load_dotenv
import time
import MySQLdb

async def fetch_all_info(service_key, app, session, semaphore):
    async with semaphore:
        tasks = [
            patent_api.get_patent_info(service_key, app, session),
            design_api.get_design_info(service_key, app, session),
            trademark_api.get_trademark_info(service_key, app, session),
        ]

        pa, de, tr = await asyncio.gather(*tasks)

        total_count = len(pa) + len(de) + len(tr)
        print(f"{app} 총 데이터 수 : {total_count}")

        return {app: {'pa': pa, 'de': de, 'tr': tr}}

def get_app_nos_from_db(limit=None):
    connection = db_connect()
    cursor = connection.cursor()
    
    # 쿼리에 LIMIT 추가
    query = "SELECT app_no FROM TB24_200"
    if limit is not None:
        query += f" LIMIT {limit}"
    
    cursor.execute(query)
    app_nos = cursor.fetchall()

    # 연결 종료
    cursor.close()
    connection.close()

    # app_no 리스트 반환
    return [app_no[0] for app_no in app_nos]

def db_connect():
    # MySQL 연결 설정
    connection = MySQLdb.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSWORD'),
        db=os.getenv('DB_NAME')
    )
    return connection

async def main():
    load_dotenv()
    service_key = os.getenv('SERVICE_KEY')

    semaphore = asyncio.Semaphore(3)  
    limit = 10  # None으로 설정하면 모든 biz_no를 처리합니다.

    # DB에서 app_no를 가져와 test_apps 리스트에 저장
    test_apps = get_app_nos_from_db(limit) 

    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks= []
        for app in test_apps:
            tasks.append(asyncio.create_task(fetch_all_info(service_key, app, session, semaphore)))
        
        results = await asyncio.gather(*tasks)
    print(results)

    end_time = time.time()
    print(f"총 걸린 시간 : {end_time - start_time}")

if __name__ == "__main__":
    asyncio.run(main())