# Copyright 2018 Cargill Incorporated
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# docker build -f sdk/python/Dockerfile-installed -t sawtooth-sdk-python-local .

# -------------=== python sdk build ===-------------

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

RUN apt-get update && apt-get install -y -q \
    python3-sawtooth-sdk=1.1.4-1

RUN mkdir -p /var/log/sawtooth

WORKDIR /project



ENTRYPOINT [ "python3", "main.py" ]

