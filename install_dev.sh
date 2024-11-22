#!/bin/bash
docker build -f ./src/install/dev/Dockerfile -t ubuntu-neojune:24.04-kor-nmp .

docker container run -itd -p 8888:80 -p 8501:8501 -p 8502:8502 -p 9091:9091 -p 9000:9000 -p 3000:3000 -p 9090:9090 -p 8081:8081 -v ./:/root/work --name neojune ubuntu-neojune:24.04-kor-nmp