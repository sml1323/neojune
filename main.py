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
    
    query = "SELECT app_no FROM TB24_200"
    if limit is not None:
        query += f" LIMIT {limit}"
    
    cursor.execute(query)
    app_nos = cursor.fetchall()

    cursor.close()
    connection.close()

    return [app_no[0] for app_no in app_nos]

def db_connect():
    connection = MySQLdb.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSWORD'),
        db=os.getenv('DB_NAME')
    )
    return connection

def map_fields(data, category):
    return {
        'ipr_seq': None,  # 필요 시 고유 ID 생성 로직 추가
        'applicant_no': data.get('applicant_no'),  # applicant_no 필드를 직접 사용하는 것이 좋습니다.
        'biz_no': data.get('biz_no', None),  # biz_no가 있을 경우 사용
        'ipr_code': category,
        'title': data.get('title'),
        'applicant': data.get('applicant'),
        'inventor': data.get('inventor', None),
        'agent': data.get('agent'),
        'ipcNumber': data.get('ipcNumber', None),
        'appl_no': data.get('appl_no'),
        'appl_date': data.get('appl_date'),
        'open_no': data.get('pub_no'),
        'open_date': data.get('pub_date'),
        'reg_no': data.get('reg_no'),
        'reg_date': data.get('reg_date'),
        'legal_status_desc': data.get('legal_status_desc'),
        'abstract': data.get('abstract', None),
        'int_appl_no': data.get('int_appl_no', None),
        'int_appl_date': data.get('int_appl_date', None),
        'int_open_no': data.get('int_open_no', None),
        'int_open_date': data.get('int_open_date', None),
        'exam_flag': data.get('exam_flag', None),
        'exam_date': data.get('exam_date', None),
        'claim_cnt': data.get('claim_cnt', 0),
        'write_time': None,
        'modify_time': None,
        'survey_year': None,
        'survey_month': None
    }

def check_duplicate(cursor, appl_no):
    query = "SELECT COUNT(*) FROM TB24_300 WHERE appl_no = %s"
    cursor.execute(query, (appl_no,))
    count = cursor.fetchone()[0]
    return count > 0

def insert_data_to_db(connection, data):
    cursor = connection.cursor()
    
    if not check_duplicate(cursor, data['appl_no']):
        query = """
        INSERT INTO TB24_300 (
            ipr_seq, applicant_no, biz_no, ipr_code, title, applicant, inventor, 
            agent, ipcNumber, appl_no, appl_date, open_no, open_date, reg_no, 
            reg_date, legal_status_desc, abstract, int_appl_no, int_appl_date, 
            int_open_no, int_open_date, exam_flag, exam_date, claim_cnt, write_time, 
            modify_time, survey_year, survey_month
        ) VALUES (
            %(ipr_seq)s, %(applicant_no)s, %(biz_no)s, %(ipr_code)s, %(title)s, %(applicant)s, %(inventor)s, 
            %(agent)s, %(ipcNumber)s, %(appl_no)s, %(appl_date)s, %(open_no)s, %(open_date)s, %(reg_no)s, 
            %(reg_date)s, %(legal_status_desc)s, %(abstract)s, %(int_appl_no)s, %(int_appl_date)s, 
            %(int_open_no)s, %(int_open_date)s, %(exam_flag)s, %(exam_date)s, %(claim_cnt)s, %(write_time)s, 
            %(modify_time)s, %(survey_year)s, %(survey_month)s
        )
        """
        cursor.execute(query, data)
        connection.commit()
        print(f"데이터 삽입 성공: {data['appl_no']}")
    else:
        print(f"중복된 데이터: {data['appl_no']}")

    cursor.close()

def process_results(results):
    connection = db_connect()
    try:
        for app, data in results.items():
            for patent_data in data.get('pa', []):
                mapped_data = map_fields(patent_data, 'PA')
                insert_data_to_db(connection, mapped_data)
            
            for design_data in data.get('de', []):
                mapped_data = map_fields(design_data, 'DE')
                insert_data_to_db(connection, mapped_data)
            
            for trademark_data in data.get('tr', []):
                mapped_data = map_fields(trademark_data, 'TR')
                insert_data_to_db(connection, mapped_data)
    finally:
        connection.close()

async def main():
    load_dotenv()
    service_key = os.getenv('SERVICE_KEY')

    semaphore = asyncio.Semaphore(3)  
    limit = 10  

    test_apps = get_app_nos_from_db(limit) 

    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for app in test_apps:
            tasks.append(asyncio.create_task(fetch_all_info(service_key, app, session, semaphore)))
        
        results = await asyncio.gather(*tasks)
    
    process_results(results)  # 결과 처리 함수 호출
    end_time = time.time()
    print(f"총 걸린 시간 : {end_time - start_time}")

if __name__ == "__main__":
    asyncio.run(main())
