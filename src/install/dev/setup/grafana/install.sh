#!/bin/bash


apt-get install musl

cd /root/work/src/install/dev/setup/grafana
wget -O grafana_11.3.1_amd64.deb https://dl.grafana.com/oss/release/grafana_11.3.1_amd64.deb

dpkg -i /root/work/src/install/dev/setup/grafana/grafana_11.3.1_amd64.deb
rm grafana_11.3.1_amd64.deb