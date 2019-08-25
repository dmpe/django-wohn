FROM python:3-slim
LABEL author="John Malc <cincenko@outlook.com>"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /wohn
WORKDIR /wohn
ADD . /wohn

RUN apt update && apt install -y software-properties-common \
      tree build-essential

RUN pip install -r requirenments.txt
EXPOSE 8000 8123

RUN chmod +x start_django.sh
CMD ["./start_django.sh"]
