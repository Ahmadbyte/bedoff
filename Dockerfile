# Python version to be used within the image
FROM python:3.8

# Ubuntu version
FROM ubuntu:18.04

RUN apt-get update

# Installing pip for managing Python packages
RUN apt-get install -y python-pip && apt-get install -y python3-pip

# Installing relevant dependencies
RUN apt-get install -y python3.8-dev

# Copy source code to the docker image
COPY . /bedoff/
WORKDIR /bedoff/

# Installing application package dependencies
RUN pip install -r requirements.txt
