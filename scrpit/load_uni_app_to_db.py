import pandas as pd
import MySQLdb
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crud.connection import db_connect
from crud.db_crud import insert_data_to_db

def get_applicant_no_from_excel(excel_file_path):
    # 엑셀 파일 읽기
    df = pd.read_excel(excel_file_path)
    # applicant_no 컬럼 데이터 가져오기
    applicant_no_data = df['applicant_no'].dropna().tolist()  # NaN 제외
    return applicant_no_data

def get_university_data():
    connection = db_connect()
    cursor = connection.cursor()
    
    # TB24_110 테이블에서 데이터 가져오기
    query = "SELECT uni_seq, applicant, biz_no, corp_no FROM TB24_110"
    cursor.execute(query)
    university_data = cursor.fetchall()  # (uni_seq, applicant, biz_no, corp_no) 튜플 리스트

    cursor.close()
    connection.close()
    return university_data

def insert_data_to_tb24_200(applicant_no_list, university_data):
    connection = db_connect()
    cursor = connection.cursor()

    # applicant_no와 university 데이터 조합하여 데이터 준비
    data_to_insert = []
    for applicant_no, (uni_seq, applicant, biz_no, corp_no) in zip(applicant_no_list, university_data):
        data_to_insert.append({
            'applicant_no': applicant_no,
            'app_seq': uni_seq,
            'app_type': 'university',
        })

    # 데이터 삽입
    insert_query = """
    INSERT INTO TB24_210 (applicant_no, app_seq, app_type)
    VALUES (%s, %s, %s)
    """
    cursor.executemany(insert_query, [(d['applicant_no'], d['app_seq'], d['app_type']) for d in data_to_insert])

    connection.commit()
    print(f"{len(data_to_insert)} records inserted successfully.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    excel_file_path_uni = '../data/TB24_210_university.xlsx'
    
    # 1단계: applicant_no 데이터 추출
    applicant_no_list = get_applicant_no_from_excel(excel_file_path_uni)
    
    # 2단계: 대학교 데이터 가져오기
    university_data = get_university_data()
    
    # 3단계: 데이터 적재
    insert_data_to_tb24_200(applicant_no_list, university_data)
