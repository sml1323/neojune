import os
from dotenv import load_dotenv
import MySQLdb
import pandas as pd

# .env 파일에서 DB 연결 정보를 로드
load_dotenv()

def db_connect():
    # MySQL 연결 설정
    connection = MySQLdb.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSWORD'),
        db=os.getenv('DB_NAME'),
        port=int(os.getenv('DB_PORT'))
    )
    return connection

# 데이터 조회 함수
def fetch_data(query):
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(data, columns=columns)
    cursor.close()
    connection.close()
    return df
