#!/bin/bash

mkdir -p logs
python -u main.py 2>&1 | tee "logs/logs $(TZ='Europe/Berlin' date '+%d.%m.%Y %H:%M').txt"