# Python version to be used within the image
FROM python:latest

# CentOS version
FROM centos:latest

# Installing relevant dependencies
RUN yum -y install net-tools
RUN yum -y install git
RUN yum -y install unixODBC-devel
RUN yum -y install gcc-c++
RUN dnf -y --enablerepo=PowerTools install libmpc-devel
RUN yum -y install gmp gmp-devel mpfr mpfr-devel libmpc
RUN yum -y install gcc && yum -y install python36-devel
RUN yum -y install which

# Installing pip for managing Python packages
RUN yum -y install epel-release && yum -y install python3-pip

# Copy source code to the docker image
COPY . /bedoff/
WORKDIR /bedoff/

# Installing application package dependencies
RUN yum -y install mysql-devel
RUN pip3 install -r requirements.txt

# Installing helpful stuff
RUN yum -y install vim-enhanced
RUN yum -y install lsof
RUN yum -y install psmisc