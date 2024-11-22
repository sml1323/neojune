#!/bin/bash

set -e  # 스크립트 실행 중 오류 발생 시 중단

# 1. Airflow 설정 디렉토리로 이동
cd src/install/public/airflow

# 2. .env 파일 생성
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

# 3. Airflow 초기화 실행
echo "Initializing Airflow..."
docker compose up airflow-init

# 4. Airflow 서비스 시작 (백그라운드에서 실행하지 않고 로그 확인)
echo "Starting Airflow services..."
docker compose up -d

# 5. Prometheus 설정 디렉토리로 이동
cd ../prometheus

# 6. Prometheus 서비스 시작 (백그라운드에서 실행하지 않고 로그 확인)
echo "Starting Prometheus services..."
docker compose up -d

# 7. Docker 이미지 빌드
cd /home/ubuntu/work/neojune
echo "Building Docker image for neojune_kipris_service..."
docker build -f ./src/install/public/Dockerfile -t neojune_kipris_service:1 .
