#!/bin/bash

# нерабочая фича. надо ставить сервисом и запускать сервисом

# just in case:
echo export JSON_SRV_HOST=10.132.0.5 > /etc/profile
echo export JSON_SRV_PORT=7070 > /etc/profile

git clone https://github.com/snvtr/runcalc-site

sudo mv /tmp/runcalc-main-app.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start runcalc-main-app
