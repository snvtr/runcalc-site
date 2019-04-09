#!/bin/bash

# нерабочая фича. надо ставить сервисом и запускать сервисом

export JSON_SRV_HOST=10.132.0.5
export JSON_SRV_PORT=7070

git clone https://github.com/snvtr/runcalc-site
cd runcalc-site/main-app
python3 run.py > log &
