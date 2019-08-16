#!/bin/bash

set -ex

python3 manage.py collectstatic
python3 manage.py makemigrations core 
python3 manage.py makemigrations userMng
python3 manage.py migrate
python3 manage.py graph_models -a -g -o output/class_diagramm.png
gunicorn vanoce.wsgi:application --log-level=info -b 127.0.0.1:8123 --workers 3