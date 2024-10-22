import pandas as pd
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import numpy as np

# .env 파일에서 DB 연결 정보를 로드
load_dotenv()

def db_connect():
    # MySQL 연결 설정
    DATABASE_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"

    # SQLAlchemy 엔진 생성
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    return session, engine



def insert_data_from_excel_to_db_com(excel_file_path , table_name):

    session, engine = db_connect()

    # 엑셀 파일 읽기
    df = pd.read_excel(excel_file_path)
    df = df.where(pd.notnull(df), None) # Nan -> None

    # 데이터프레임을 딕셔너리 리스트로 변환
    data_to_insert = df.drop(columns=['company_seq']).to_dict(orient='records')

    # 데이터베이스에 한꺼번에 삽입
    with engine.connect() as connection:
        metadata = MetaData()
        company_info = Table(table_name, metadata,  autoload_with=engine)

        # bulk insert로 한꺼번에 데이터를 삽입
        connection.execute(company_info.insert(), data_to_insert)
        connection.commit() 

    print(f"{len(df)} records inserted successfully.")

def insert_data_from_excel_to_db_uni(excel_file_path, table_name):

    session, engine = db_connect()

    # 엑셀 파일 읽기
    df = pd.read_excel(excel_file_path)

    # 시간 방식 변경
    df['write_time'] = df['write_time'].replace({'오후': 'PM', '오전': 'AM'}, regex=True)
    df['write_time'] = pd.to_datetime(df['write_time'], format='%Y-%m-%d %p %I:%M:%S', errors='coerce') # 날짜 방식 변경
    df['write_time'] = df['write_time'].dt.strftime('%Y-%m-%d %H:%M:%S')

    df = df.replace({np.nan: None}) # Nan -> None

    data_to_insert = df.to_dict(orient='records')

     # 데이터베이스에 한꺼번에 삽입
    with engine.connect() as connection:
        metadata = MetaData()
        university_info = Table(table_name, metadata,  autoload_with=engine)

        # bulk insert로 한꺼번에 데이터를 삽입
        connection.execute(university_info.insert(), data_to_insert)
        connection.commit() 

    print(f"{len(df)} records inserted successfully.")


if __name__ == "__main__":
    # excel_file_path_com = '../data/TB24_100_company_info.xlsx'
    # insert_data_from_excel_to_db_com(excel_file_path_com, 'company_info')

    excel_file_path_uni = '../data/TB24_210_university.xlsx'
    insert_data_from_excel_to_db_uni(excel_file_path_uni , 'university_info')
