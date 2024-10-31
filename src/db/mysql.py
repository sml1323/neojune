import os
from typing import List, Dict, Optional, Tuple
from dotenv import load_dotenv
import MySQLdb
load_dotenv()

class Mysql:
    def __init__(self):
        # .env 파일에서 DB 연결 정보를 로드
        pass
        
    def _db_connect(self):
        # MySQL 연결 설정
        connection = MySQLdb.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            passwd=os.getenv('DB_PASSWORD'),
            db=os.getenv('DB_NAME')
        )
        return connection

    def insert_data_to_db(self,
                         cursor,
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

    def fetch_data_by_page(self,
                          cursor, 
                          table_name: str, 
                          page: int, 
                          page_size: int,
                          columns: List[str] = None,
                          filter_condition: str = None
        ) -> Tuple[Tuple]:
        """
        페이지 단위로 데이터를 가져오는 함수.
        
        :param cursor: MySQL 커서 객체
        :param table_name: 조회할 테이블 이름
        :param page: 현재 페이지 번호 (1부터 시작)
        :param page_size: 한 페이지당 가져올 데이터 수
        :return: 조회된 데이터 (리스트 형식)
        """

        # OFFSET 계산
        offset = (page - 1) * page_size

        # 조회할 컬럼 선택, 없을 경우 모든 컬럼('*')
        if columns:
            columns_str = ', '.join(columns)
        else:
            columns_str = '*'

        # 필터 조건이 있는 경우와 없는 경우의 쿼리 작성
        if filter_condition:
            sql = f"""
                SELECT {columns_str} FROM {table_name}
                WHERE {filter_condition}
                LIMIT %s OFFSET %s
            """
        else:
            sql = f"""
                SELECT {columns_str} FROM {table_name}
                LIMIT %s OFFSET %s
            """
        
        # 쿼리 실행 및 데이터 가져오기
        cursor.execute(sql, (page_size, offset))
        rows = cursor.fetchall()

        return rows

    def upsert_data(self, 
                    table_name: str, 
                    data: List[Dict]
                    ) -> None:
        """
        주어진 데이터를 특정 테이블에 삽입하거나 갱신하는 함수.

        :param table_name: 데이터를 삽입하거나 업데이트할 테이블의 이름입니다.
        :param data: 삽입 또는 갱신할 데이터의 목록으로, 각 항목은 컬럼과 값을 포함한 딕셔너리입니다.
        :return: None
            데이터가 없으면 함수는 아무 작업 없이 종료됩니다.
        """

        # 데이터가 없으면 함수 종료
        if not data:
            print("No data to insert.")
            return
        
        connection = self._db_connect()
        cursor = connection.cursor()

        columns = data[0].keys()
        placeholders = ', '.join(['%s'] * len(columns))

        # 공통적인 업데이트 구문
        common_update_clause = """
            legal_status_desc = VALUES(legal_status_desc),
            pub_num = VALUES(pub_num),
            pub_date = VALUES(pub_date)
        """

        # 테이블 이름에 따른 추가 업데이트 구문
        if table_name in ["TB24_design", "TB2_patent"]:
            additional_update_clause = """
                reg_no = VALUES(reg_no),
                reg_date = VALUES(reg_date),
                open_no = VALUES(open_no),
                open_date = VALUES(open_date),
            """
        else:
            additional_update_clause = ""

        # SQL 쿼리 준비
        sql = f"""
            INSERT INTO {table_name} ({', '.join(columns)}) 
            VALUES ({placeholders})
            ON DUPLICATE KEY UPDATE
            {additional_update_clause}
            {common_update_clause};
        """

        data_values = [tuple(d.values()) for d in data]
        cursor.executemany(sql, data_values)

        connection.commit()

        cursor.close()
        connection.close()

    def fetch_data_from_db(self,
                          table_name: str, 
                          columns: List[str] = None, 
                          limit: int = None, 
                          filter_condition: str = None
                          ) -> List[Tuple]:
        """
        데이터베이스에서 데이터를 가져오는 범용 함수.
        
        :param table_name: 조회할 테이블 이름
        :param columns: 조회할 컬럼 목록 (기본값은 모든 컬럼)
        :param limit: 가져올 최대 데이터 수
        :param filter_condition: 필터 조건 (WHERE 절에 해당)
        :return: 조회된 데이터 리스트
        """
        
        connection = self._db_connect()
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
            sql += f" ORDER BY applicant_id ASC LIMIT {limit}"
        
        # 쿼리 실행 및 데이터 가져오기
        cursor.execute(sql)
        rows = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        return rows