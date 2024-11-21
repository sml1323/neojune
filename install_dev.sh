#!/bin/bash
docker build -f ./src/install/dev/Dockerfile -t ubuntu-neojune:24.04-kor-nmp .

docker container run -itd -p 8888:80 -p 8501:8501 -p 8502:8502 -p 5000:5000 -p 5001:5001 -p 5002:5002 -p 5003:5003 -v ./:/root/work --name neojune2 ubuntu-neojune:24.04-kor-nmp