{% if cookiecutter.include_rocksdb.lower() == "y" %}
FROM marcosschroh/rocksdb:0.0.1

{% else %}
FROM python:3.7-slim

RUN echo 'deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main' >> /etc/apt/sources.list \
    && apt-get update
{% endif %}

RUN apt-get install -y --no-install-recommends apt-utils \
    && apt-get install -y netcat && apt-get autoremove -y \
    && apt-get install gcc make g++ libgflags-dev libsnappy-dev zlib1g-dev libbz2-dev liblz4-dev libzstd-dev -y

ENV PIP_FORMAT=legacy
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Create unprivileged user
RUN adduser --disabled-password --gecos '' myuser

WORKDIR /{{cookiecutter.project_slug}}/

COPY . /{{cookiecutter.project_slug}}

RUN pip3 install -e .

ENTRYPOINT ["./run.sh"]

