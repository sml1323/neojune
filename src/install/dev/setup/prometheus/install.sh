#!/bin/bash

mkdir -p /root/app

cd /root/work/src/install/dev/setup/prometheus

wget -O prometheus-3.0.0.linux-amd64.tar.gz https://github.com/prometheus/prometheus/releases/download/v3.0.0/prometheus-3.0.0.linux-amd64.tar.gz

wget -O pushgateway-1.9.0.linux-amd64.tar.gz https://github.com/prometheus/pushgateway/releases/download/v1.9.0/pushgateway-1.9.0.linux-amd64.tar.gz


tar -xvf prometheus-3.0.0.linux-amd64.tar.gz 
tar -xvf pushgateway-1.9.0.linux-amd64.tar.gz

echo "압축 해제 완료"

mv prometheus-3.0.0.linux-amd64 /root/app
mv pushgateway-1.9.0.linux-amd64 /root/app
cp prometheus.yml /root/app/prometheus-3.0.0.linux-amd64

echo "이동 완료"

rm prometheus-3.0.0.linux-amd64.tar.gz
rm pushgateway-1.9.0.linux-amd64.tar.gz

echo "삭제 완료"