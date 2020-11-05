FROM ubuntu:18.04

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

RUN apt-get update
RUN apt-get install -y python3 \
    python3-dev \
    vim \
    python3-pip \
    locales \
    wget \
    unzip \
    python3-lxml

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

RUN pip3 install -r /tmp/requirements.txt

RUN ln -s /usr/bin/python3  /usr/bin/python
RUN ln -s /usr/bin/pip3  /usr/bin/pip
