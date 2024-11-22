from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime
from pendulum import timezone
import os
import subprocess

# 처리 엔티티 목록
entities = [
    "company_design", "company_patent", "company_trademark",
    "university_design", "university_patent", "university_trademark"
]

# 작업 디렉토리 설정
WORK_DIR = os.getenv('WORK_DIR', '/root/work')  # 기본값은 '/root/work'
MAIN_PY_PATH = os.path.join(WORK_DIR, 'main.py')  # main.py의 경로


# 공통 태스크 생성 함수
def execute_task(module, task_name):
    command = f'python {MAIN_PY_PATH} {module} {task_name}'
    subprocess.run(command, shell=True, check=True, cwd=WORK_DIR)


# PythonOperator 생성 함수
def create_task(task_id, module, task_name):
    return PythonOperator(
        task_id=task_id,
        python_callable=execute_task,
        op_args=[module, task_name],  # 'task' 대신 'task_name'으로 변경
    )


# DAG 정의
with DAG(
    'all_task_dev-1.0',
    default_args={'retries': 1},
    description='A DAG with PythonOperator tasks for XML, SQL, and DB processing',
    schedule_interval='0 7 * * *',
    start_date=datetime(2023, 1, 1, tzinfo=timezone('Asia/Seoul')),
    catchup=False,
) as dag:

    # XML 처리 태스크 그룹
    with TaskGroup(group_id='xml_processing') as xml_group:
        prev_task = None
        for entity in entities:
            task = create_task(f'run_xml_{entity}', 'save_to_xml', entity)
            if prev_task:
                prev_task >> task
            prev_task = task

    # SQL 처리 태스크 그룹 (병렬 실행)
    with TaskGroup(group_id='sql_processing') as sql_group:
        for entity in entities:
            create_task(f'run_sql_{entity}', 'xml_to_sql', entity)

    # Base 작업 그룹
    with TaskGroup(group_id='base_processing') as base_group:
        prev_task = None
        for entity in entities:
            task = create_task(f'run_base_{entity}', 'sql_to_db', f'base {entity}')
            if prev_task:
                prev_task >> task
            prev_task = task

    # IPC/CPC 작업 그룹
    with TaskGroup(group_id='ipc_cpc_processing') as ipc_cpc_group:
        prev_task = None
        for entity in ["company_patent", "university_patent"]:
            task = create_task(f'run_ipc_cpc_{entity}', 'sql_to_db', f'ipc_cpc {entity}')
            if prev_task:
                prev_task >> task
            prev_task = task

    # Priority 작업 그룹
    with TaskGroup(group_id='priority_processing') as priority_group:
        prev_task = None
        for entity in ["company_design", "company_trademark", "university_design", "university_trademark"]:
            task = create_task(f'run_priority_{entity}', 'sql_to_db', f'priority {entity}')
            if prev_task:
                prev_task >> task
            prev_task = task

    # dict_to_sql_sub 처리 태스크 그룹 (순차 실행)
    with TaskGroup(group_id='dict_to_sql_sub_processing') as dict_group:
        prev_task = None
        for entity in entities:
            task = create_task(f'run_dict_{entity}', 'dict_to_sql_sub', entity)
            if prev_task:
                prev_task >> task
            prev_task = task

    # 태스크 그룹 간 연결
    xml_group >> sql_group >> base_group >> dict_group >> ipc_cpc_group >> priority_group
