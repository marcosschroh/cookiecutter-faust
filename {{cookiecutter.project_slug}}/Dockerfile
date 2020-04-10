{% if cookiecutter.include_rocksdb.lower() == "y" %}
FROM marcosschroh/rocksdb:0.0.1

RUN apt-get install -y --no-install-recommends apt-utils \
    && apt-get install -y netcat && apt-get autoremove -y \
    && apt-get install gcc make g++ libgflags-dev libsnappy-dev zlib1g-dev libbz2-dev liblz4-dev libzstd-dev -y

{% else %}
FROM python:3.7-slim

RUN echo 'deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main' >> /etc/apt/sources.list \
    && apt-get update && apt-get install -y netcat make && apt-get autoremove -y
{% endif %}

ENV PIP_FORMAT=legacy
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /{{cookiecutter.project_slug}}/

COPY . /{{cookiecutter.project_slug}}

RUN make install-production

{% if cookiecutter.include_rocksdb.lower() == "y" %}
RUN yes Y | apt-get remove --purge git libgflags-dev libsnappy-dev zlib1g-dev libbz2-dev liblz4-dev libzstd-dev
{% endif %}

# Create unprivileged user
RUN groupadd --non-unique --gid 1000 faust && adduser --disabled-password --uid 1000 --gid 1000 faust
RUN chown -R faust:faust /{{cookiecutter.project_slug}}
USER faust

ENTRYPOINT ["./scripts/run"]
