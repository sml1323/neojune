#!/bin/bash
docker build -f ./src/install/dev/Dockerfile -t ubuntu-neojune:24.04-kor-nmp .

docker container run -itd -p 8888:80 -v ./:/root/work --name neojune ubuntu-neojune:24.04-kor-nmp