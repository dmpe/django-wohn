FROM python:latest
MAINTAINER John Malc <cincenko@outlook.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /wohn
WORKDIR /wohn
ADD . /wohn

RUN pip install -r requirenments.txt
EXPOSE 8000

RUN chmod +x start_django.sh
CMD ["./start_django.sh"]
#CMD exec gunicorn vanoce.wsgi:application --bind 0.0.0.0:8000 --workers 3
#CMD ["gunicorn", "-b", "0.0.0.0:8000", "vanoce.wsgi:application", "--workers", "3"]

