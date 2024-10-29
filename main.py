import asyncio
import aiohttp
from api_modules import design_api, patent_api, trademark_api
import os
from dotenv import load_dotenv
import time
import MySQLdb
from datetime import datetime
import xml.etree.ElementTree as ET
import xml.etree.ElementTree as ET


# XML 저장 함수
def save_data_as_xml(data_dict, file_name):
    root = ET.Element("")

    for applicant, (applicant_id, data) in data_dict.items():
        response_elem = ET.SubElement(root, "response")

        # <applicant> 태그 추가
        applicant_tag = ET.SubElement(response_elem, "applicant")
        applicant_tag.text = str(applicant_id)

        # <header> 태그 추가 (결과 코드와 메시지를 포함)
        header = ET.SubElement(response_elem, "header")
        ET.SubElement(header, "resultCode")
        ET.SubElement(header, "resultMsg")

        # <body> 태그 추가 및 그 안에 <items> 데이터 삽입
        body = ET.SubElement(response_elem, "body")
        items_elem = ET.SubElement(body, "items")
        
        # data 내부에 있는 XML 콘텐츠를 <items>에 추가
        for content in data['data']:
            original_data = ET.fromstring(content)

            # 기존 XML에서 <items> 내부 태그들만 추가
            items = original_data.find(".//items")
            if items is not None:
                for elem in items:
                    items_elem.append(elem)

    # XML 파일로 저장
    tree = ET.ElementTree(root)
    file_path = f"./save_to_xml/{file_name}.xml"
    tree.write(file_path, encoding="utf-8", xml_declaration=True)
    print(f"{file_path} 저장 완료")
# DB에서 app_no와 applicant_id 목록을 가져오는 함수
def get_app_nos_from_db(limit=None):
    connection = db_connect()
    cursor = connection.cursor()

    query = "SELECT app_no, applicant_id FROM TB24_200"
    if limit is not None:
        query += f" LIMIT {limit}"

    cursor.execute(query)
    app_nos = cursor.fetchall()
    cursor.close()
    connection.close()

    # 각 레코드를 (app_no, applicant_id) 쌍으로 반환
    return [(app_no[0], app_no[1]) for app_no in app_nos]

# MySQL 연결 함수
def db_connect():
    connection = MySQLdb.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSWORD'),
        db=os.getenv('DB_NAME')
    )
    return connection

async def fetch_all_info(service_key, app_no, applicant_id, session, semaphore, pa_dict, de_dict, tr_dict):
    async with semaphore:
        tasks = [
            asyncio.create_task(patent_api.get_patent_info(service_key, app_no, session)),
            asyncio.create_task(design_api.get_design_info(service_key, app_no, session)),
            asyncio.create_task(trademark_api.get_trademark_info(service_key, app_no, session)),
        ]

        results = await asyncio.gather(*tasks)

        # data 부분만 추출하여 딕셔너리에 저장
        pa_dict[app_no] = (applicant_id, results[0])
        de_dict[app_no] = (applicant_id, results[1])
        tr_dict[app_no] = (applicant_id, results[2])

        total_count = sum(len(data['data']) for data in results)
        print(f"{app_no} 총 데이터 수 : {total_count}")

async def main():
    load_dotenv()
    service_key = os.getenv('SERVICE_KEY')
    semaphore = asyncio.Semaphore(40)
    limit = 5
    test_apps = get_app_nos_from_db(limit)
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

    # data 부분만 XML 파일로 저장
    save_data_as_xml(pa_dict, f"patent_data_{timestamp}")
    save_data_as_xml(de_dict, f"design_data_{timestamp}")
    save_data_as_xml(tr_dict, f"trademark_data_{timestamp}")
    print("모든 데이터를 XML 파일로 저장 완료")

if __name__ == '__main__':
    asyncio.run(main())
