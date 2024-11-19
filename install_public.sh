#!/bin/bash
docker build -f ./src/install/public/Dockerfile -t neojune_kipris_service:3.0 .

# docker container run -itd --name neojune_kipris_service neojune_kipris_service:2.0
