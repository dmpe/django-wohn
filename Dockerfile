FROM python:latest
LABEL author="John Malc <cincenko@outlook.com>"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /wohn
WORKDIR /wohn
ADD . /wohn

RUN pip install -r requirenments.txt
EXPOSE 8000

RUN chmod +x start_django.sh
CMD ["./start_django.sh"]
#CMD exec gunicorn melive.wsgi:application --bind 0.0.0.0:8000 --workers 3
#CMD ["gunicorn", "-b", "0.0.0.0:8000", "melive.wsgi:application", "--workers", "3"]

