#!/bin/bash

set -ex

# Clear the existing files before trying to copy or link the original file.
python3 manage.py collectstatic --no-input
python3 manage.py makemigrations core userMng --no-input
python3 manage.py migrate
python3 manage.py graph_models -a -g -o output/class_diagramm.png
gunicorn melive.wsgi:application --log-level=info -b :8123 --workers 3
