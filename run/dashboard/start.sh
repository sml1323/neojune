#!/bin/bash

cd /root/work/run/dashboard

# 서버 실행 (백그라운드로 실행하면서 출력 숨기기)
airflow/start.sh > /dev/null 2>&1 &
grafana/start.sh > /dev/null 2>&1 &
prometheus/start.sh > /dev/null 2>&1 &
pushgateway/start.sh > /dev/null 2>&1 &
flask/start.sh > /dev/null 2>&1 &
streamlit/start.sh > /dev/null 2>&1 &


# 모든 서비스 준비 완료 메시지 출력
# clear  # 기존 출력 내용 모두 지우기
echo "=================================="
echo "id: admin"
echo "password: admin"
echo "=================================="
echo "airflow: http://localhost:8080"
echo "grafana: http://localhost:3000"
echo "prometheus: http://localhost:9090"
echo "pushgateway: http://localhost:9091"
echo "flask: http://localhost:5000"
echo "streamlit: http://localhost:8501"
echo "=================================="
