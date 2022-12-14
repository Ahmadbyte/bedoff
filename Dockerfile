# Python version to be used within the image
FROM python:3.8

# Ubuntu version
FROM ubuntu:18.04

RUN apt-get update -y

# Configure pdfkit
RUN apt install wkhtmltopdf -y
RUN apt install xvfb -y
RUN mv /usr/bin/wkhtmltopdf /usr/bin/wkhtmltopdf_bin
RUN mkdir /opt/wkhtmltopdf_conf/

ADD wkhtmltopdf.sh /opt/wkhtmltopdf_conf/
RUN chmod +x /opt/wkhtmltopdf_conf/wkhtmltopdf.sh
RUN ln -s /opt/wkhtmltopdf_conf/wkhtmltopdf.sh /usr/bin/wkhtmltopdf

# Installing pip for managing Python packages
RUN apt-get install -y python3-pip
RUN apt-get install -y libmysqlclient-dev

# Installing relevant dependencies
RUN apt-get install -y python3.8-dev


# Copy source code to the docker image
COPY . /bedoff/
WORKDIR /bedoff/

# Installing application package dependencies
RUN pip3 install -r requirements.txt
