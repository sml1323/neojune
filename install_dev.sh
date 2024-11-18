#!/bin/bash
docker build -f ./src/dockerfile/Dockerfile_dev -t ubuntu-neojune:24.04-kor-nmp .

docker container run -itd -p 80:8080 -v ./:/root/work --name neojune ubuntu-neojune:24.04-kor-nmp