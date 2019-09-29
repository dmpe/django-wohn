FROM python:latest
LABEL author="John Malc <cincenko@outlook.com>"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /wohn
WORKDIR /wohn
ADD . /wohn

RUN apt update && \
    apt install -y nano tree locate graphviz libgraphviz-dev && \
    pip install -r requirenments.txt && \
    chmod +x start_django.sh

EXPOSE 8000 8123

# TODO: set entrypoint once container can start
# ENTRYPOINT ["./start_django.sh"]
CMD ["./start_django.sh"]
