from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

# 호스트에 XML 파일이 저장될 경로
host_output_path = "/home/ubuntu/app/res/output"

# 공통 태스크 생성 함수
def create_task(task_id, command, dag):
    return DockerOperator(
        task_id=task_id,
        image='neojune_kipris_service:1.3',
        mount_tmp_dir=False,
        do_xcom_push=False, 
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
    'neojune_parallel',
    default_args={'retries': 1},
    description='A DAG with DockerOperator tasks for XML and SQL processing',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # XML 처리 태스크 구성
    xml_tasks = [
        create_task('run_xml_company_design', 'python main.py --run save_to_xml company_design', dag),
        create_task('run_xml_company_patent', 'python main.py --run save_to_xml company_patent', dag),
        create_task('run_xml_company_trademark', 'python main.py --run save_to_xml company_trademark', dag),
        create_task('run_xml_univ_design', 'python main.py --run save_to_xml university_design', dag),
        create_task('run_xml_univ_patent', 'python main.py --run save_to_xml university_patent', dag),
        create_task('run_xml_univ_trademark', 'python main.py --run save_to_xml university_trademark', dag),
    ]

    # SQL 처리 태스크 구성 (병렬 실행될 태스크)
    sql_tasks = [
        create_task('run_sql_company_design', 'python main.py --run xml_to_sql company_design', dag),
        create_task('run_sql_company_patent', 'python main.py --run xml_to_sql company_patent', dag),
        create_task('run_sql_company_trademark', 'python main.py --run xml_to_sql company_trademark', dag),
        create_task('run_sql_univ_design', 'python main.py --run xml_to_sql university_design', dag),
        create_task('run_sql_univ_patent', 'python main.py --run xml_to_sql university_patent', dag),
        create_task('run_sql_univ_trademark', 'python main.py --run xml_to_sql university_trademark', dag),
    ]

    # XML 태스크들을 순차적으로 실행
    for i in range(len(xml_tasks) - 1):
        xml_tasks[i] >> xml_tasks[i + 1]

    # XML 태스크 그룹이 완료된 후 SQL 태스크들이 병렬로 실행되도록 설정
    final_xml_task = xml_tasks[-1]
    for sql_task in sql_tasks:
        final_xml_task >> sql_task
