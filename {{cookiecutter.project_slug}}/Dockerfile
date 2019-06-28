FROM python:3.7-slim

RUN echo 'deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main' >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends apt-utils

ENV PIP_FORMAT=legacy
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get install -y netcat && apt-get autoremove -y

# Create unprivileged user
RUN adduser --disabled-password --gecos '' myuser

{% if cookiecutter.include_rocksdb.lower() == "y" %}
#Install RocksDB
ENV DEBIAN_FRONTEND noninteractive
ENV DEBIAN_FRONTEND teletype
RUN apt-get upgrade -y gcc
RUN apt-get install git make g++ libgflags-dev libsnappy-dev zlib1g-dev libbz2-dev liblz4-dev libzstd-dev -y

RUN git clone https://github.com/facebook/rocksdb.git /tmp/rocksdb
WORKDIR /tmp/rocksdb
RUN make shared_lib INSTALL_PATH=/usr
RUN make install-shared
RUN rm -rf /tmp/rocksdb

ENV CGO_CFLAGS  "-I/usr/local/include"
ENV CGO_LDFLAGS "-L/usr/local/lib -lrocksdb -lstdc++ -lm -lz -lbz2 -lsnappy"
ENV LD_LIBRARY_PATH "/usr/local/lib"
ENV STORE_URI=rocksdb://
{% endif %}

WORKDIR /{{cookiecutter.project_slug}}/

COPY . /{{cookiecutter.project_slug}}

RUN pip3 install -e .

ENTRYPOINT ["./run.sh"]

