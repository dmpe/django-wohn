FROM python:latest
LABEL author="John Malc <cincenko@outlook.com>"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /wohn && \
    apt update && \
    apt install -y nano tree locate graphviz libgraphviz-dev

WORKDIR /wohn
ADD . /wohn

RUN pip install -r requirenments.txt && \
    chmod +x start_django.sh

EXPOSE 8000 8123
ENTRYPOINT ["./start_django.sh"]
