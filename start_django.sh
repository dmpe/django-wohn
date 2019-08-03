#!/usr/bin/env bash

set -ex

python3 manage.py collectstatic
python3 manage.py makemigrations core 
python3 manage.py makemigrations userMng
python3 manage.py migrate
gunicorn vanoce.wsgi:application --log-level=info -b 0.0.0.0:8123 --workers 3