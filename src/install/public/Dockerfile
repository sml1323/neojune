FROM python:3.12

WORKDIR /app

COPY . .

# 필요한 패키지 설치
RUN apt-get update && \
    apt-get install -y pkg-config libmariadb-dev libmariadb-dev-compat libdbus-1-dev cmake libcairo2-dev libgirepository1.0-dev && \
    rm -rf /var/lib/apt/lists/*  # 캐시 제거로 이미지 크기 줄이기

# Python 라이브러리 설치
RUN pip install -r /app/requirements.txt
