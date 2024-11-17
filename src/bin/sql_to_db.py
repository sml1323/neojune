from ..db.mysql import Mysql
from ..util import util
import os


base_path = f"res/output/{util.get_timestamp()}/sql"
company_path = f"{base_path}/company"
university_path = f"{base_path}/university"

mysql = Mysql()


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



def run_company_design():
    execute_sql_files_in_directory(company_path, "design", mysql)
    execute_sql_files_in_directory(company_path  + "/priority" , "priority_design", mysql)


def run_company_patent():
    execute_sql_files_in_directory(company_path, "patent", mysql)
    execute_sql_files_in_directory(company_path + "/ipc_cpc", "ipc_cpc", mysql)

def run_company_trademark():
    execute_sql_files_in_directory(company_path, "trademark", mysql)
    execute_sql_files_in_directory(company_path + "/priority", "priority_trademark", mysql)



def run_university_design():
    execute_sql_files_in_directory(university_path, "design", mysql)
    execute_sql_files_in_directory(university_path + "/priority", "priority_design", mysql)


def run_university_patent():
    execute_sql_files_in_directory(university_path, "patent", mysql)
    execute_sql_files_in_directory(university_path + "/ipc_cpc", "ipc_cpc", mysql)


def run_university_trademark():
    execute_sql_files_in_directory(university_path, "trademark", mysql)
    execute_sql_files_in_directory(university_path + "/priority", "priority_trademark", mysql)





def main():
    run_company_design()
    run_company_patent()
    run_company_trademark()
    run_university_design()
    run_university_patent()
    run_university_trademark()
    pass
