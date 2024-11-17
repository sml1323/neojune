from ...db.mysql import Mysql
from ...util import util

# base 부터 먼저 실행 후 나머지 실행

base_path = f"res/output/{util.get_timestamp()}/sql"
company_path = f"{base_path}/company"
university_path = f"{base_path}/university"

mysql = Mysql()


def run_company_design():
    util.execute_sql_files_in_directory(company_path  + "/priority" , "priority_design", mysql)


def run_company_trademark():
    util.execute_sql_files_in_directory(company_path + "/priority", "priority_trademark", mysql)


def run_university_design():
    util.execute_sql_files_in_directory(university_path + "/priority", "priority_design", mysql)


def run_university_trademark():
    util.execute_sql_files_in_directory(university_path + "/priority", "priority_trademark", mysql)



def main():
    run_company_design()
    run_company_trademark()
    run_university_design()
    run_university_trademark()
    pass