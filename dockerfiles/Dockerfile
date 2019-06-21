FROM python:latest
MAINTAINER John Malc <cincenko@outlook.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

RUN mkdir /wohn
WORKDIR /wohn

ADD . /wohn/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000
CMD exec gunicorn vanoce.wsgi:application --bind 0.0.0.0:8000 --workers 3