{{cookiecutter.project_name}}
{{ '=' * cookiecutter.project_name|length }}

{{cookiecutter.description}}

{% if cookiecutter.open_source_license != "Not open source" %}
:License: {{cookiecutter.open_source_license}}
{% endif %}

Installation
------------

Install local requirements:

```bash
make install
```

Usage
------

If you do not have a cluster running locally you can use `docker-compose` to avoid several headaches.
By default the `KAFKA_BOOTSTRAP_SERVER` is `kafka://localhost:29092`.

```bash
make kafka-cluster
```

Then, start the `Faust application`:

```bash
make start-app
```

Settings
--------

Settings are created based on [local-settings](https://github.com/drgarcia1986/simple-settings) package.

The only settings required if the `KAFKA_BOOTSTRAP_SERVER` environment variable.

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

The settings also include a basic logging configuration:

```python
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

Basic Commands
--------------

* Start application: `make kafka-cluster`. This command start both the *Page Views* application
* Stop and remove containers: `make stop-kafka-cluster`
* Install requirements: `make install`
* Start Faust application: `make start-app`
* List topics: `make list-topics`
* Create topic: `make create-topic={topic-name}`
* List agents: `make list-agents`
* Send events to page_view topic/agent: `make send-page-view-event payload='{"id": "foo", "user": "bar"}'`

Docker
------

The `Dockerfile` is based on  `python:3.7-slim`.

Docker Compose
--------------

`docker-compose.yaml` includes `zookeepeer`, `kafka` and `schema-registry` (if included in the cookiecutter setup) based on `confluent-inc`.
For more information you can go to [confluentinc](https://docs.confluent.io/current/installation/docker/docs/index.html) and see the docker compose example [here](https://github.com/confluentinc/cp-docker-images/blob/master/examples/cp-all-in-one/docker-compose.yml#L23-L48)

Useful ENVIRONMENT variables that you may change:

|Variable| description  | example |
|--------|--------------|---------|
| WORKER_PORT | Worker port | `6066` |
| KAFKA_BOOTSTRAP_SERVER | Kafka servers | `kafka://localhost:29092` |
| KAFKA_BOOTSTRAP_SERVER_NAME | Kafka server name| `kafka` |
| KAFKA_BOOTSTRAP_SERVER_PORT | Kafka server port | `29092` |
| SCHEMA_REGISTRY_SERVER | Schema registry server name | `schema-registry` |
| SCHEMA_REGISTRY_SERVER_PORT | Schema registry server port | `8081` |
| SCHEMA_REGISTRY_URL | Schema Registry Server url | `http://schema-registry:8081` |

Run tests
---------

```sh
./scripts/test.sh
```

Lint code
---------

```sh
./scripts/lint
```

Type checks
-----------

Running type checks with mypy:

```sh
mypy {{cookiecutter.project_slug}}
```
