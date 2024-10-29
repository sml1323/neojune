import os
import sys
import time
from dotenv import load_dotenv
import asyncio

# 프로젝트 루트 디렉토리 절대 경로 추가
sys.path.append('/root/work/neojune')

from crud.connection import db_connect
from crud.db_crud import *
from api_modules.biz_api import process_applicants  # 필요한 함수만 import

# 나머지 코드는 그대로 유지
start = time.time()

connection = db_connect()
cursor = connection.cursor()
service_key = os.getenv('SERVICE_KEY')

page = 1
total_data = []
page_size = 48

while True:
    rows = fetch_data_by_page(cursor, 'TB24_100', page=page, page_size=page_size)
    if rows:
        result = asyncio.run(process_applicants(service_key, rows))
        total_data.extend(result)
        page += 1
    else:
        break

insert_data_to_db(cursor, 'TB24_200', total_data, True)
connection.commit()

cursor.close()
connection.close()

end = time.time()
print(end - start)
