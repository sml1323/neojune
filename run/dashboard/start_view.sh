#!/bin/bash

cd /root/work/run/dashboard

# 서버 실행 (백그라운드로 실행하면서 출력 숨기기)
streamlit/start.sh > /dev/null 2>&1 &
flask/start.sh > /dev/null 2>&1 &


# 모든 서비스 준비 완료 메시지 출력
# clear  # 기존 출력 내용 모두 지우기
echo "=================================="
echo "streamlit: http://localhost:8501"
echo "flask: http://localhost:5000"
echo "=================================="
