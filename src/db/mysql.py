import os
from typing import List, Dict, Optional, Tuple
from dotenv import load_dotenv
import MySQLdb, json

load_dotenv()

class Mysql:
    def __init__(self):
        # .env 파일에서 DB 연결 정보를 로드
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.db_name = os.getenv('DB_NAME')
        self.db_port = int(os.getenv('DB_PORT'))
        self.connection = None  # DB 연결을 저장할 속성
        self._connect_to_db()  # 초기 연결 설정

    def _connect_to_db(self):
        """DB에 연결하고 self.connection에 저장"""
        if not self.connection or not self.connection.open:
            self.connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db_name,
                port=self.db_port
            )

    def _get_cursor(self):
        """연결 상태를 확인하고 커서를 반환"""
        self._connect_to_db()  # 필요 시 연결을 재설정
        return self.connection.cursor()

    def get_cursor_fetchall(self, sql, *args) -> List[list]:
            with self._get_cursor() as cursor:
                cursor.execute(sql, *args)
                return json.loads(json.dumps(cursor.fetchall()))
            
    def insert_data_to_db(self,
                         table_name: str,
                         data_to_insert: List[Dict[str, Optional[str]]], 
                         use_executemany: bool = True
                        ) -> None:
        """
        데이터베이스에 데이터를 삽입하는 함수.
        
        :param table_name: 삽입할 테이블 이름
        :param data_to_insert: 삽입할 데이터 리스트 (딕셔너리 형태의 리스트)
        :param use_executemany: True면 executemany 사용, False면 execute 사용
        """
        
        if not data_to_insert:
            print("No data to insert.")
            return
        
        columns = data_to_insert[0].keys()
        sql = f"""
            INSERT INTO {table_name} ({', '.join(columns)}) 
            VALUES ({', '.join(['%s'] * len(columns))})
        """
        data_values = [tuple(data.values()) for data in data_to_insert]

        with self._get_cursor() as cursor:
            if use_executemany:
                cursor.executemany(sql, data_values)
            else:
                for data in data_values:
                    cursor.execute(sql, data)
            self.connection.commit()

    def fetch_data_by_page(self, 
                          table_name: str, 
                          page: int, 
                          page_size: int,
                          columns: List[str] = None,
                          filter_condition: str = None
        ) -> List[Tuple]:
        """
        페이지 단위로 데이터를 가져오는 함수.
        
        :param table_name: 조회할 테이블 이름
        :param page: 현재 페이지 번호 (1부터 시작)
        :param page_size: 한 페이지당 가져올 데이터 수
        :return: 조회된 데이터 리스트
        """
        
        offset = (page - 1) * page_size
        columns_str = ', '.join(columns) if columns else '*'
        sql = f"SELECT {columns_str} FROM {table_name}"

        if filter_condition:
            sql += f" WHERE {filter_condition}"
        
        sql += " LIMIT %s OFFSET %s"
        
        with self._get_cursor() as cursor:
            cursor.execute(sql, (page_size, offset))
            rows = cursor.fetchall()

        return rows

    def upsert_data(self, 
                    table_name: str, 
                    data: List[Dict]
                    ) -> None:
        """
        주어진 데이터를 특정 테이블에 삽입하거나 갱신하는 함수.

        :param table_name: 데이터를 삽입하거나 업데이트할 테이블 이름
        :param data: 삽입 또는 갱신할 데이터 리스트 (딕셔너리 형태의 리스트)
        """
        
        if not data:
            print("No data to insert.")
            return
        
        columns = data[0].keys()
        placeholders = ', '.join(['%s'] * len(columns))
        
        common_update_clause = """
            legal_status_desc = VALUES(legal_status_desc),
            pub_num = VALUES(pub_num),
            pub_date = VALUES(pub_date)
        """
        
        additional_update_clause = """
            reg_no = VALUES(reg_no),
            reg_date = VALUES(reg_date),
            open_no = VALUES(open_no),
            open_date = VALUES(open_date),
        """ if table_name in ["TB24_design", "TB2_patent"] else ""
        
        sql = f"""
            INSERT INTO {table_name} ({', '.join(columns)}) 
            VALUES ({placeholders})
            ON DUPLICATE KEY UPDATE
            {additional_update_clause}
            {common_update_clause};
        """
        
        data_values = [tuple(d.values()) for d in data]
        
        with self._get_cursor() as cursor:
            cursor.executemany(sql, data_values)
            self.connection.commit()

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
        
        columns_str = ', '.join(columns) if columns else '*'
        sql = f"SELECT {columns_str} FROM {table_name}"

        if filter_condition:
            sql += f" WHERE {filter_condition}"
        
        if limit:
            sql += f" ORDER BY applicant_id ASC LIMIT {limit}"
        
        with self._get_cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

        return rows

    def get_limit_company_no_id(self, limit=1) -> list[list]:
        sql = f'SELECT applicant_no, applicant_id FROM TB24_200 LIMIT {limit}'
        return self.get_cursor_fetchall(sql)

    def get_all_company_no_id(self, ) -> list[list]:
        sql = f'SELECT applicant_no, applicant_id FROM TB24_200'
        return self.get_cursor_fetchall(sql)

    def get_limit_university_no_id(self, limit=1) -> list[list]:
        sql = f'SELECT applicant_no, applicant_id FROM TB24_210 LIMIT {limit}'
        return self.get_cursor_fetchall(sql)

    def get_all_university_no_id(self, ) -> list[list]:
        sql = f'SELECT applicant_no, applicant_id FROM TB24_210'
        return self.get_cursor_fetchall(sql)


    def close_connection(self):
        """연결 닫기"""
        if self.connection and self.connection.open:
            self.connection.close()
