from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.task_group import TaskGroup
from docker.types import Mount
from datetime import datetime
from pendulum import timezone  # pendulum의 timezone을 import

# 호스트에 XML 파일이 저장될 경로
host_output_path = "/home/ubuntu/app/res/output"

# 공통 태스크 생성 함수
def create_task(task_id, module, task):
    return DockerOperator(
        task_id=task_id,
        image='neojune_kipris_service_prometheus:1.7',
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
    'kipris_without_runsql_all_data',
    default_args={'retries': 1},
    description='A DAG with DockerOperator tasks for XML, SQL, and DB processing',
    start_date=datetime(2023, 1, 1, tzinfo=timezone('Asia/Seoul')),
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
                prev_task >> task  
            prev_task = task

    # SQL 처리 태스크 그룹 (병렬 실행)
    with TaskGroup(group_id='sql_processing') as sql_group:
        for entity in entities:
            create_task(f'run_sql_{entity}', 'xml_to_sql', entity)

    # 태스크 그룹 간 연결
    xml_group >> sql_group 
