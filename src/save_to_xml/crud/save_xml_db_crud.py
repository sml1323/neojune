import os
from typing import List, Dict, Optional

import MySQLdb
from crud.save_xml_connection import db_connect

def insert_data_to_db(cursor,
                     table_name: str,
                     data_to_insert: List[Dict[str, Optional[str]]], 
                     use_executemany: bool = True
                    ) -> None:
    """
    데이터베이스에 데이터를 삽입하는 함수.
    
    :param cursor: MySQL 커서 객체
    :param table_name: 삽입할 테이블 이름
    :param data_to_insert: 삽입할 데이터 리스트 (딕셔너리 형태의 리스트)
    :param use_executemany: True면 executemany 사용, False면 execute 사용
    """

    # 데이터가 없으면 함수 종료
    if not data_to_insert:
        print("No data to insert.")
        return

    # 첫 번째 데이터의 키를 통해 컬럼 이름 추출
    columns = data_to_insert[0].keys()

    # SQL 쿼리 준비
    sql = f"""
        INSERT INTO {table_name} ({', '.join(columns)}) 
        VALUES ({', '.join(['%s'] * len(columns))})
    """

    # 데이터 삽입을 위한 값 준비
    data_values = [tuple(data.values()) for data in data_to_insert]

    # executemany 사용 여부에 따라 실행 방식 변경
    if use_executemany:
        cursor.executemany(sql, data_values)
    else:
        for data in data_values:
            cursor.execute(sql, data)


def fetch_data_from_db(table_name: str, 
                       columns: list[str] = None, 
                       limit: int = None, 
                       filter_condition: str = None) -> list[tuple]:
    """
    데이터베이스에서 데이터를 가져오는 범용 함수.
    
    :param table_name: 조회할 테이블 이름
    :param columns: 조회할 컬럼 목록 (기본값은 모든 컬럼)
    :param limit: 가져올 최대 데이터 수
    :param filter_condition: 필터 조건 (WHERE 절에 해당)
    :return: 조회된 데이터 리스트
    """
    
    connection = db_connect()
    cursor = connection.cursor()
    
    # 조회할 컬럼 지정, 없으면 모든 컬럼('*') 조회
    columns_str = ', '.join(columns) if columns else '*'
    
    # 기본 SQL 쿼리 작성
    sql = f"SELECT {columns_str} FROM {table_name}"
    
    # 필터 조건이 있으면 WHERE 절 추가
    if filter_condition:
        sql += f" WHERE {filter_condition}"
        
    # 제한된 결과 개수가 설정된 경우 LIMIT 추가
    if limit:
        sql += f" order by applicant_id asc LIMIT {limit}"
    
    # 쿼리 실행 및 데이터 가져오기
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return rows
