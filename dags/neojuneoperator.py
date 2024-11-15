from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

# 호스트에 XML 파일이 저장될 경로
host_output_path = "/home/ubuntu/app/res/output"

with DAG(
    'docker_operator_neojune',
    default_args={'retries': 1},
    description='A DAG with DockerOperator tasks for company XML processing',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    xml_company_design_task = DockerOperator(
        task_id='run_xml_company_design',
        image='before_final:1',
        api_version='auto',
        auto_remove=True,
        command="python main.py --run save_to_xml company_design",  
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

    xml_company_patent_task = DockerOperator(
        task_id='run_xml_company_patent',
        image='before_final:1',
        api_version='auto',
        auto_remove=True,
        command="python main.py --run save_to_xml company_patent",
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

    xml_company_trademark_task = DockerOperator(
        task_id='run_xml_company_trademark',
        image='before_final:1',
        api_version='auto',
        auto_remove=True,
        command="python main.py --run save_to_xml company_trademark", 
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

    xml_university_design_task = DockerOperator(
        task_id='run_xml_univ_design',
        image='before_final:1',
        api_version='auto',
        auto_remove=True,
        command="python main.py --run save_to_xml university_design",  
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


    xml_university_patent_task = DockerOperator(
        task_id='run_xml_univ_patent',
        image='before_final:1',
        api_version='auto',
        auto_remove=True,
        command="python main.py --run save_to_xml university_patent",  
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

    xml_university_trademark_task = DockerOperator(
        task_id='run_xml_univ_trademark',
        image='before_final:1',
        api_version='auto',
        auto_remove=True,
        command="python main.py --run save_to_xml university_trademark",  
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


    sql_company_design_task = DockerOperator(
        task_id='run_sql_company_design',
        image='before_final:1',
        api_version='auto',
        auto_remove=True,
        command="python main.py --run xml_to_sql company_design", 
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
    sql_company_patent_task = DockerOperator(
        task_id='run_sql_company_patent',
        image='before_final:1',
        api_version='auto',
        auto_remove=True,
        command="python main.py --run xml_to_sql company_patent",  
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
    sql_company_trademark_task = DockerOperator(
        task_id='run_sql_company_trademark',
        image='before_final:1',
        api_version='auto',
        auto_remove=True,
        command="python main.py --run xml_to_sql company_trademark", 
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

    sql_university_design_task = DockerOperator(
        task_id='run_sql_univ_design',
        image='before_final:1',
        api_version='auto',
        auto_remove=True,
        command="python main.py --run xml_to_sql university_design",
        docker_url ='unix://var/run/docker.sock',
        network_mode='bridge',
        mounts=[
            {
                "source": host_output_path,
                "target": "/app/res/output",
                "type": "bind"
            }
        ]
    )

    sql_university_patent_task = DockerOperator(
        task_id='run_sql_univ_patent',
        image='before_final:1',
        api_version='auto',
        auto_remove=True,
        command='python main.py --run xml_to_sql university_patent',
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

    sql_university_trademark_task = DockerOperator(
        task_id='run_sql_univ_trademark',
        image='before_final:1',
        api_version='auto',
        auto_remove=True,
        command='python main.py --run xml_to_sql university_trademark',
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


    xml_company_design_task >> xml_company_patent_task >> xml_company_trademark_task >> \
    xml_university_design_task >> xml_university_patent_task >> xml_university_trademark_task >> \
    sql_company_design_task >> sql_company_patent_task >> sql_company_trademark_task >> \
    sql_university_design_task >> sql_university_patent_task >> sql_university_trademark_task

