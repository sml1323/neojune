from ...db.mysql import Mysql
from ...util import util


import os


def main(is_main = True):
    base_path = f"res/output/{util.get_timestamp()}/sql"
    # base_path = f"res/output/20241114/sql"
    company_path = f"{base_path}/company"
    university_path = f"{base_path}/university"

    mysql = Mysql()


    # 본보기
    # util.execute_sql_files_in_directory(company_path, "patent", mysql)
    # util.execute_sql_files_in_directory(company_path + "/ipc_cpc", "ipc_cpc", mysql)
    # 이렇게 한쌍으로 모두 적용



    # 각 디렉토리와 접두사(prefix)에 대해 SQL 파일들을 실행
    if is_main:
        util.execute_sql_files_in_directory(company_path, "design", mysql)
        util.execute_sql_files_in_directory(company_path, "patent", mysql)
        util.execute_sql_files_in_directory(company_path, "trademark", mysql)
        util.execute_sql_files_in_directory(university_path, "design", mysql)
        util.execute_sql_files_in_directory(university_path, "patent", mysql)
        util.execute_sql_files_in_directory(university_path, "trademark", mysql)
    else:
        util.execute_sql_files_in_directory(company_path  + "/priority" , "priority_design", mysql)
        util.execute_sql_files_in_directory(company_path + "/ipc_cpc", "ipc_cpc", mysql)
        util.execute_sql_files_in_directory(company_path + "/priority", "priority_trademark", mysql)
        util.execute_sql_files_in_directory(university_path + "/priority", "priority_design", mysql)
        util.execute_sql_files_in_directory(university_path + "/ipc_cpc", "ipc_cpc", mysql)
        util.execute_sql_files_in_directory(university_path + "/priority", "priority_trademark", mysql)
