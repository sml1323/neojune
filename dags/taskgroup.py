from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.task_group import TaskGroup
from docker.types import Mount
from datetime import datetime

# 호스트에 XML 파일이 저장될 경로
host_output_path = "/home/ubuntu/app/res/output"

# 공통 태스크 생성 함수
def create_task(task_id, command):
    return DockerOperator(
        task_id=task_id,
        image='neojune_kipris_service:1.3',
        api_version='auto',
        auto_remove=True,
        command=command,
        mount_tmp_dir=False,
        do_xcom_push=False, 
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        mounts=[
            Mount(
                source=host_output_path,
                target="/app/res/output",
                type="bind"
            )
        ],
    )

with DAG(
    'neojune_short_operator',
    default_args={'retries': 1},
    description='A DAG with DockerOperator tasks for XML and SQL processing',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # XML 및 SQL 태스크 이름과 명령어 매핑
    entities = ["company_design", "company_patent", "company_trademark",
                "university_design", "university_patent", "university_trademark"]

    # XML 처리 태스크 그룹
    with TaskGroup(group_id='xml_processing') as xml_group:
        prev_task = None
        for entity in entities:
            task = create_task(f'run_xml_{entity}', f'python main.py --run save_to_xml {entity}')
            if prev_task:
                prev_task >> task  # 이전 태스크와 현재 태스크를 순차적으로 연결
            prev_task = task

    # SQL 처리 태스크 그룹
    with TaskGroup(group_id='sql_processing') as sql_group:
        for entity in entities:
            create_task(f'run_sql_{entity}', f'python main.py --run xml_to_sql {entity}')

    # DB 처리 태스크 그룹
    # with TaskGroup(group_id='db_processing') as db_group:
    #     for entity in entities:
    #         create_task(f'run_db_{entity}', f'python main.py --run sql_to_db {entity}')

    # 태스크 그룹 간 연결
    xml_group >> sql_group
