from ...db.mysql import Mysql
from ...util import util
from ...enum.Config import Config

# base 부터 먼저 실행 후 나머지 실행

base_path = f"{Config.OUTPUT_PATH.value}/{util.get_timestamp()}/sql"

company_path = f"{base_path}/company"
university_path = f"{base_path}/university"

mysql = Mysql()

def run_company_patent():
    util.execute_sql_files_in_directory(company_path + "/ipc_cpc", "ipc_cpc", mysql)


def run_university_patent():
    util.execute_sql_files_in_directory(university_path + "/ipc_cpc", "ipc_cpc", mysql)



def main():
    run_company_patent()
    run_university_patent()
    pass
