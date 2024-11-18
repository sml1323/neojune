from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

# 호스트에 XML 파일이 저장될 경로
host_output_path = "/home/ubuntu/app/res/output"

# 공통 태스크 생성 함수
def create_task(task_id, command, dag):
    return DockerOperator(
        task_id=task_id,
        image='neojune_kipris_service:1.0',
        api_version='auto',
        auto_remove=True,
        command=command,
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        mounts=[
            {
                "source": host_output_path,
                "target": "/app/res/output",
                "type": "bind"
            }
        ],
        dag=dag
    )

with DAG(
    'neojune_short_code',
    default_args={'retries': 1},
    description='A DAG with DockerOperator tasks for XML and SQL processing',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # 태스크 파라미터 정의
    tasks_config = [
        ('run_xml_company_design', 'python main.py --run save_to_xml company_design'),
        ('run_xml_company_patent', 'python main.py --run save_to_xml company_patent'),
        ('run_xml_company_trademark', 'python main.py --run save_to_xml company_trademark'),
        ('run_xml_univ_design', 'python main.py --run save_to_xml university_design'),
        ('run_xml_univ_patent', 'python main.py --run save_to_xml university_patent'),
        ('run_xml_univ_trademark', 'python main.py --run save_to_xml university_trademark'),
        ('run_sql_company_design', 'python main.py --run xml_to_sql company_design'),
        ('run_sql_company_patent', 'python main.py --run xml_to_sql company_patent'),
        ('run_sql_company_trademark', 'python main.py --run xml_to_sql company_trademark'),
        ('run_sql_univ_design', 'python main.py --run xml_to_sql university_design'),
        ('run_sql_univ_patent', 'python main.py --run xml_to_sql university_patent'),
        ('run_sql_univ_trademark', 'python main.py --run xml_to_sql university_trademark')
    ]

    # 태스크 생성 및 순서 정의
    previous_task = None
    for task_id, command in tasks_config:
        task = create_task(task_id=task_id, command=command, dag=dag)
        if previous_task:
            previous_task >> task
        previous_task = task
