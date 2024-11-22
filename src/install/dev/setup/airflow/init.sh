#!/bin/bash

airflow db init
airflow users create \
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com

ln -s /root/work/src/install/dev/setup/airflow/dags /root/airflow/dags

# Airflow 설정 파일 경로
AIRFLOW_CFG="/root/airflow/airflow.cfg"

# 수정할 dags_folder 경로
DAGS_FOLDER="/root/work/src/install/dev/setup/airflow/dags"

# dags_folder 설정을 수정
sed -i "s|^dags_folder =.*|dags_folder = $DAGS_FOLDER|" $AIRFLOW_CFG

sed -i "s|^load_examples *=.*|load_examples = False|" $AIRFLOW_CFG

# 변경 확인
echo "$AIRFLOW_CFG의 설정이 완료 됐습니다."
