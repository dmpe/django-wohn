FROM python:latest
MAINTAINER John Malc <cincenko@outlook.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && \
	apt-get install -y gcc gcc-multilib && \
    rm -rf /var/lib/apt/lists/* 

RUN mkdir /wohn
WORKDIR /wohn
ADD . /wohn

# Install any needed packages specified in requirenments.txt
RUN pip install -r requirenments.txt
EXPOSE 8000

RUN chmod +x start_django.sh
ENTRYPOINT ["./start_django.sh"]
#CMD exec gunicorn vanoce.wsgi:application --bind 0.0.0.0:8000 --workers 3
#CMD ["gunicorn", "-b", "0.0.0.0:8000", "vanoce.wsgi:application", "--workers", "3"]

