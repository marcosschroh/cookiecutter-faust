FROM python:3.7-slim
    
RUN echo 'deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main' >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends apt-utils

ENV PIP_FORMAT=legacy
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get install -y netcat && apt-get autoremove -y

# Create unprivileged user
RUN adduser --disabled-password --gecos '' myuser

WORKDIR /{{cookiecutter.project_slug}}/

# As configured in docker-compose.yaml the copy built in the image is replaced
# with a volume mount of the host directory. The volume is mounted at run time
# but not build time.
COPY . /{{cookiecutter.project_slug}}

RUN pip3 -r requirements.txt

ENTRYPOINT ["./run.sh"]

