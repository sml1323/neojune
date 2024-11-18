from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.task_group import TaskGroup
from docker.types import Mount
from datetime import datetime

# 호스트에 XML 파일이 저장될 경로
host_output_path = "/home/ubuntu/app/res/output"

# 공통 태스크 생성 함수
def create_task(task_id, module, task):
    return DockerOperator(
        task_id=task_id,
        image='neojune_kipris_service:2.0',
        api_version='auto',
        auto_remove=True,
        command=f'python main.py {module} {task}',
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
    'neojune_final-1.0',
    default_args={'retries': 1},
    description='A DAG with DockerOperator tasks for XML, SQL, and DB processing',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # 처리 엔티티 목록
    entities = ["company_design", "company_patent", "company_trademark",
                "university_design", "university_patent", "university_trademark"]


    # XML 처리 태스크 그룹
    with TaskGroup(group_id='xml_processing') as xml_group:
        prev_task = None
        for entity in entities:
            task = create_task(f'run_xml_{entity}', 'save_to_xml', entity)
            if prev_task:
                prev_task >> task  # 태스크를 순차적으로 연결
            prev_task = task

    # SQL 처리 태스크 그룹 (병렬 실행)
    with TaskGroup(group_id='sql_processing') as sql_group:
        for entity in entities:
            create_task(f'run_sql_{entity}', 'xml_to_sql', entity)

    # DB 처리 태스크 그룹
    with TaskGroup(group_id='db_processing') as db_group:

        # Base 작업
        with TaskGroup(group_id='base_processing') as base_group:
            prev_task = None
            for entity in entities:
                task = create_task(f'run_base_{entity}', 'sql_to_db', f'base {entity}')
                if prev_task:
                    prev_task >> task  # 태스크를 순차적으로 연결
                prev_task = task

        # IPC/CPC 작업
        with TaskGroup(group_id='ipc_cpc_processing') as ipc_cpc_group:
            prev_task = None
            for entity in ["company_patent", "university_patent"]:
                task = create_task(f'run_ipc_cpc_{entity}', 'sql_to_db', f'ipc_cpc {entity}')
                if prev_task:
                    prev_task >> task  # 태스크를 순차적으로 연결
                prev_task = task

        # Priority 작업
        with TaskGroup(group_id='priority_processing') as priority_group:
            prev_task = None
            for entity in ["company_design", "company_trademark", "university_design", "university_trademark"]:
                task = create_task(f'run_priority_{entity}', 'sql_to_db', f'priority {entity}')
                if prev_task:
                    prev_task >> task  # 태스크를 순차적으로 연결
                prev_task = task

        # DB 작업 그룹 연결
        base_group >> ipc_cpc_group >> priority_group


    # 태스크 그룹 간 연결
    xml_group >> sql_group >> db_group
