# Cookiecutter Faust

[![Build Status](https://travis-ci.org/marcosschroh/cookiecutter-faust.svg?branch=master)](https://travis-ci.org/marcosschroh/cookiecutter-faust)
[![GitHub license](https://img.shields.io/github/license/marcosschroh/cookiecutter-faust.svg)](https://github.com/marcosschroh/cookiecutter-faust/blob/feature/add-license-and-remove-network-after-clean/LICENSE)

## Table of Contents

  - [Features](#features)
  - [Usage](#usage)
  - [Useful Commands](#useful-commands)
  - [Settings](#settings)
  - [Docker and Docker Compose](#docker-and-docker-compose)
  - [Development](#development)

### Features

- Python 3.7+
- Docker-compose for local development that builds a `kafka` cluster
- Useful commands included in Makefile
- Kubernetes manifests included
- CI generated (Gitlab/Travis)
- Settings that include logging, minimal Faust and SSL configuration
- Faust agent example with a test case
- Option to use `rocksDB` as a Faust data store

### Usage

Let's pretend you want to create a Faust project called `super faust`...

First, install `Cookiecutter`:

```bash
pip install "cookiecutter"
```

Now run it against this repo:

```bash
cookiecutter https://github.com/marcosschroh/cookiecutter-faust
```

You'll be prompted for some values. Provide them, then a Faust project will be created for you
based on the convention of medium/large project mentioned above

Answer the prompts with your own desired options. For example:

```bash
project_name [My Awesome Faust Project]: super faust
project_slug [super_faust]:
description [My Awesome Faust Project!]:
long_description [My Awesome Faust Project!]:
author_name [Marcos Schroh]:
author_email [marcos-schroh@gmail.com]:
version [0.1.0]:
Select open_source_license:
1 - MIT
2 - BSD
3 - GPLv3
4 - Apache Software License 2.0
5 - Not open source
Choose from 1, 2, 3, 4, 5 (1, 2, 3, 4, 5) [1]:
worker_port [6066]:
Select log_level:
1 - CRITICAL
2 - ERROR
3 - WARNING
4 - INFO
5 - DEBUG
6 - NOTSET
Choose from 1, 2, 3, 4, 5, 6 (1, 2, 3, 4, 5, 6) [1]: 4
include_schema_registry [y]:
include_rocksdb [y]:
Select ci_provider:
1 - travis
2 - gitlab
3 - none
Choose from 1, 2 (1, 2) [1]: 2
```

Enter the project and take a look around:

```bash
cd super_faust/
ls

CONTRIBUTORS.txt  Dockerfile  LICENSE  Makefile  README.md  docker-compose.yaml setup.cfg  pyproject.py  super_faust
```

Now time to run it. In a terminal located at the project root directory folder start the `kafka cluster`:

```bash
make kafka-cluster
```

In another terminal, run the `Faust application`:

```bash
make install
make start-app
```

Now you will see the project starting. If you chose to have the [page view tutorial]((https://faust.readthedocs.io/en/latest/playbooks/pageviews.html)), you can send events to the `page_views` topic. In a different terminal also at the project root directory execute:

```bash
make send-page-view-event payload='{"id": "foo", "user": "bar"}'
```

and in the first terminal you will see the logs of the event received.

![Running Project](docs/img/cookiecutter-faust.gif)

Optional, create a git repo and push it there:

```bash
git init
git add .
git commit -m "first awesome commit"
git remote add origin git@github.com:marcosschroh/super-faust.git
git push -u origin master
```

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

### Useful Commands

|Command|Description| Default values|Example|
|-------|------------|--------------|-------|
| `make kafka-cluster`      | Run the kafka cluster          |      ---        | |
| `make stop-kafka-cluster`      |  Stop kafka cluster, clean containers and network         |     ---         | |
| `make install`      |  Install local requirements         |     ---         | |
| `make start-app`      |  Start Faust application        |     ---         | |
| `make bash service={the-service}`      |  Access to container         |   service=kafka           | `make bash` |
| `make list-topics`      |      List topics     |    ---          | |
| `make create-topic replication-factor={replication-factor} --partitions={number-of-partitions topic-name={your-topic-name}`      |  Create topic         |  replication-factor=1 partitions=1.           |  `make create-topic topic-name=test-topic`|
| `make send-page-view-event payload='{a payload}'`| Send event to a page view application | -- | `make send-page-view-event payload='{"id": "foo", "user": "bar"}'` |
| `make list-agents`| List faust agents| --- | |

### Settings

Settings are created based on [local-settings](https://github.com/drgarcia1986/simple-settings) package.

The only settings required if the `KAFKA SERVER` environment variable which by default is `KAFKA_BOOTSTRAP_SERVER`

```python
SIMPLE_SETTINGS = {
    'OVERRIDE_BY_ENV': True,
    'CONFIGURE_LOGGING': True,
    'REQUIRED_SETTINGS': ('KAFKA_BOOTSTRAP_SERVER', 'STORE_URI'),
}

# The following variables can be ovirriden from ENV
KAFKA_BOOTSTRAP_SERVER = "kafka://localhost:29092"

TOPIC_ALLOW_DECLARE = True
TOPIC_DISABLE_LEADER = False

SSL_ENABLED = False
SSL_CONTEXT = None

if SSL_ENABLED:
    # file in pem format containing the client certificate, as well as any ca certificates
    # needed to establish the certificate’s authenticity
    KAFKA_SSL_CERT = None

    # filename containing the client private key
    KAFKA_SSL_KEY = None

    # filename of ca file to use in certificate verification
    KAFKA_SSL_CABUNDLE = None

    # password for decrypting the client private key
    SSL_KEY_PASSWORD = None

    SSL_CONTEXT = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=KAFKA_SSL_CABUNDLE)

    SSL_CONTEXT.load_cert_chain(KAFKA_SSL_CERT, keyfile=KAFKA_SSL_KEY, password=SSL_KEY_PASSWORD)
```

The settings also include a basic logging and store configuration:

```python
STORE_URI = "rocksdb://" # If rocksdb is  disabled is "memory://"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': '{{cookiecutter.log_level}}',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        'page_views': {
            'handlers': ['console'],
            'level': '{{cookiecutter.log_level}}',
        },
    },
}
```

### Docker and Docker Compose

The `Dockerfile` is based on  `python:3.7-slim`. The example is [here](https://github.com/marcosschroh/cookiecutter-faust/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/Dockerfile)

The `docker-compose.yaml` includes `zookeeper`, `kafka` and `schema-registry` (if selected for inclusion) based on `confluent-inc`.
For more information you can go to [confluentinc](https://docs.confluent.io/current/installation/docker/docs/index.html) and see the docker compose example [here](https://github.com/confluentinc/examples/blob/5.3.1-post/cp-all-in-one/docker-compose.yml)

Useful `ENVIRONMENT` variables that you may change:

|Variable| description  | default |
|--------|--------------|---------|
| WORKER_PORT | Worker port | Autogenerated by `cookiecutter`. |
| KAFKA_BOOTSTRAP_SERVER | Kafka servers. | `kafka://localhost:29092` |
| KAFKA_BOOTSTRAP_SERVER_NAME | Kafka server name| `kafka` |
| KAFKA_BOOTSTRAP_SERVER_PORT | Kafka server port | `29092` |
| SCHEMA_REGISTRY_SERVER | Schema registry server name | `schema-registry` |
| SCHEMA_REGISTRY_SERVER_PORT | Schema registry server port | `8081` |
| SCHEMA_REGISTRY_URL | Schema Registry Server url | `http://schema-registry:8081` |

### Development

Run tests:

```bash
./scripts/test
```

Run code linting

```bash
./scripts/lint
```
