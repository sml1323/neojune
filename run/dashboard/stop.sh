#!/bin/bash

pkill -f airflow
pkill -f grafana
pkill -f prometheus
pkill -f pushgateway
pkill -f flask
pkill -f streamlit