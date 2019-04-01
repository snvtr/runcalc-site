#!/bin/bash

cd /srv/www/

python3 -m http.server --cgi 8000
