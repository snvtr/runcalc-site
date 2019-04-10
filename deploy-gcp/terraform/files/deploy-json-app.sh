#!/bin/bash

# нерабочая фича. надо ставить сервисом и запускать сервисом

git clone https://github.com/snvtr/runcalc-site

sudo mv /tmp/runcalc-json-app.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start runcalc-json-app