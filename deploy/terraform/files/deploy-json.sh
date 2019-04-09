#!/bin/bash

# нерабочая фича. надо ставить сервисом и запускать сервисом

git clone https://github.com/snvtr/runcalc-site
cd runcalc-site/json-app
python3 vdot.py > log &
