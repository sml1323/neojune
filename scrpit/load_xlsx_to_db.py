import os
import sys

import pandas as pd
import MySQLdb
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crud.connection import db_connect
from crud.db_crud import insert_data_to_db

# 변환 함수
def format_biz_no(biz_no):
    if biz_no is None:
        return None
    return f"{biz_no[:3]}-{biz_no[3:5]}-{biz_no[5:]}"  # 220-88-87953

def format_corp_no(corp_no):
    if corp_no is None:
        return None
    return f"{corp_no[:6]}-{corp_no[6:]}" 

def insert_data_from_excel_to_db_com(excel_file_path, table_name):
    connection = db_connect()
    cursor = connection.cursor()

    # 엑셀 파일 읽기
    df = pd.read_excel(excel_file_path)
    df = df.where(pd.notnull(df), None)  # Nan -> None

    # biz_no와 corp_no 포맷 변경
    df['biz_no'] = df['biz_no'].astype(str).apply(format_biz_no)
    df['corp_no'] = df['corp_no'].apply(format_corp_no)

    # (추가)필요한 컬럼만 선택
    required_columns = ['biz_no', 'corp_no', 'biz_type', 'company_name']
    df = df[required_columns]

    # (수정)데이터프레임을 딕셔너리 리스트로 변환
    data_to_insert = df.to_dict(orient='records')

    insert_data_to_db(cursor, table_name, data_to_insert, True)
    connection.commit()
    
    print(f"{len(df)} records inserted successfully.")

    cursor.close()
    connection.close()


def insert_data_from_excel_to_db_uni(excel_file_path, table_name):

    connection = db_connect()
    cursor = connection.cursor()

    # 엑셀 파일 읽기
    df = pd.read_excel(excel_file_path)

    # 시간 방식 변경
    df['write_time'] = df['write_time'].replace({'오후': 'PM', '오전': 'AM'}, regex=True)
    df['write_time'] = pd.to_datetime(df['write_time'], format='%Y-%m-%d %p %I:%M:%S', errors='coerce') # 날짜 방식 변경
    df['write_time'] = df['write_time'].dt.strftime('%Y-%m-%d %H:%M:%S')

    # (수정)형식 변경
    df['biz_no'] = df['biz_no'].apply(format_biz_no)
    df['corp_no'] = df['corp_no'].apply(format_corp_no)

    # (추가)필요한 컬럼만 선택
    required_columns = ['biz_no', 'corp_no', 'applicant']
    df = df[required_columns]

    df = df.replace({np.nan: None}) # Nan -> None

    data_to_insert = df.to_dict(orient='records')

    insert_data_to_db(cursor, table_name, data_to_insert, True )
    connection.commit()
    
    print(f"{len(df)} records inserted successfully.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    
    excel_file_path_com = '../data/TB24_100_company_info.xlsx'
    insert_data_from_excel_to_db_com(excel_file_path_com, 'TB24_100')

    excel_file_path_uni = '../data/TB24_210_university.xlsx'
    insert_data_from_excel_to_db_uni(excel_file_path_uni , 'TB24_110')