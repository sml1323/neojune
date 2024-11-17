from ...db.mysql import Mysql
from ...util import util


import os

def execute_sql_files_in_directory(directory: str, prefix: str, mysql):
    """
    지정된 디렉토리에서 특정 접두사(prefix)를 가진 SQL 파일들을 순서대로 실행합니다.
    """
    # 디렉토리에서 해당 prefix로 시작하는 파일만 필터링하고 정렬
    sql_files = sorted(
        [f for f in os.listdir(directory) if f.startswith(prefix) and f.endswith(".sql")]
    )

    # 각 파일을 SQL로 실행
    for sql_file in sql_files:
        sql_file_path = os.path.join(directory, sql_file)
        print(sql_file_path)
        mysql.execute_sql_file(sql_file_path)
        print(f"Executed {sql_file_path}")

def main(is_main = True):
    base_path = f"res/output/{util.get_timestamp()}/sql"
    # base_path = f"res/output/20241114/sql"
    company_path = f"{base_path}/company"
    university_path = f"{base_path}/university"

    mysql = Mysql()


    # 본보기
    # execute_sql_files_in_directory(company_path, "patent", mysql)
    # execute_sql_files_in_directory(company_path + "/ipc_cpc", "ipc_cpc", mysql)
    # 이렇게 한쌍으로 모두 적용



    # 각 디렉토리와 접두사(prefix)에 대해 SQL 파일들을 실행
    if is_main:
        execute_sql_files_in_directory(company_path, "design", mysql)
        execute_sql_files_in_directory(company_path, "patent", mysql)
        execute_sql_files_in_directory(company_path, "trademark", mysql)
        execute_sql_files_in_directory(university_path, "design", mysql)
        execute_sql_files_in_directory(university_path, "patent", mysql)
        execute_sql_files_in_directory(university_path, "trademark", mysql)
    else:
        execute_sql_files_in_directory(company_path  + "/priority" , "priority_design", mysql)
        execute_sql_files_in_directory(company_path + "/ipc_cpc", "ipc_cpc", mysql)
        execute_sql_files_in_directory(company_path + "/priority", "priority_trademark", mysql)
        execute_sql_files_in_directory(university_path + "/priority", "priority_design", mysql)
        execute_sql_files_in_directory(university_path + "/ipc_cpc", "ipc_cpc", mysql)
        execute_sql_files_in_directory(university_path + "/priority", "priority_trademark", mysql)
