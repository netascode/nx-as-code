FROM ubuntu:bionic

# Install prerequisities for Ansible
RUN apt-get update
RUN apt-get -y install python3 python3-nacl python3-pip libffi-dev

# Install ansible
RUN pip3 install ansible
RUN pip3 install --upgrade pip setuptools

# Install requirements
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "/bin/sh" , "-c"]