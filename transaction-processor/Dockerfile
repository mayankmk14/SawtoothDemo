
FROM ubuntu:xenial

ENV VERSION=AUTO_STRICT

RUN \
    if [ ! -z $HTTP_PROXY ] && [ -z $http_proxy ]; then \
    http_proxy=$HTTP_PROXY; \
    fi; \
    if [ ! -z $HTTPS_PROXY ] && [ -z $https_proxy ]; then \
    https_proxy=$HTTPS_PROXY; \
    fi; \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 8AA7AF1F1091A5FD \
    && echo "deb [arch=amd64] http://repo.sawtooth.me/ubuntu/bumper/stable xenial universe" >> /etc/apt/sources.list \
    && apt-get update

RUN apt-get install -y -q --allow-downgrades \
    python3 \
    python3-pip

RUN pip3 install --upgrade pip

RUN pip install sawtooth-sdk==1.1.4.post1

RUN mkdir -p /var/log/sawtooth

WORKDIR /project



ENTRYPOINT [ "python3", "-u", "main.py" ]
