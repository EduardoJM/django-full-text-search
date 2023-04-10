FROM python:3.9

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /opt/app/requirements.txt
RUN chmod +x /opt/app/requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update -y
RUN apt-get install -y python3-dev netcat

COPY . /opt/app/
