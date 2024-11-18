from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

# 호스트에 XML 파일이 저장될 경로
host_output_path = "/home/ubuntu/app/res/output"

with DAG(
    'docker_operator_with_two_tasks',
    default_args={'retries': 1},
    description='A DAG with two sequential DockerOperator tasks',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # 첫 번째 태스크: main.py 실행
    task1 = DockerOperator(
        task_id='run_main',
        image='test3:2task',
        api_version='auto',
        auto_remove=True,
        command="python main.py",
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        mounts=[
            {
                "source": host_output_path,
                "target": "/app/res/output",
                "type": "bind"
            }
        ]
    )

    # 두 번째 태스크: main2.py 실행
    task2 = DockerOperator(
        task_id='run_main2',
        image='test3:2task',
        api_version='auto',
        auto_remove=True,
        command="python main2.py",
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        mounts=[
            {
                "source": host_output_path,
                "target": "/app/res/output",
                "type": "bind"
            }
        ]
    )

    # task1 완료 후 task2 실행
    task1 >> task2
