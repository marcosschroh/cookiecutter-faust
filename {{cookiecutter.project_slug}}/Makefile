PARTITIONS=1
REPLICATION-FACTOR=1

# For local development
export WORKER_PORT={{cookiecutter.worker_port}}
export SIMPLE_SETTINGS={{cookiecutter.project_slug}}.settings

PYTHON?=python3.7

# Installation
install:
	$(PYTHON) -m venv ./venv
	./venv/bin/pip install -U pip -r requirements/base.txt

install-test:
	$(PYTHON) -m venv ./venv
	./venv/bin/pip install -U pip -r requirements/test.txt

install-production:
	$(PYTHON) -m venv ./venv
	./venv/bin/pip install -U pip -r requirements/production.txt

bash:
	docker-compose run --user=$(shell id -u) ${service} bash

# Build docker compose
restart:
	docker-compose restart ${service}

logs:
	docker-compose logs

# Removes old containers, free's up some space
remove:
	# Try this if this fails: docker rm -f $(docker ps -a -q)
	docker-compose rm --force -v

remove-network:
	docker network rm {{cookiecutter.project_slug}}_default || true

stop:
	docker-compose stop

kafka-cluster:
	docker-compose up

stop-kafka-cluster: stop remove remove-network

# Kafka related
list-topics:
	docker-compose exec kafka kafka-topics --list --zookeeper zookeeper:32181

create-topic:
	docker-compose exec kafka kafka-topics --create --zookeeper zookeeper:32181 --replication-factor ${REPLICATION-FACTOR} --partitions ${PARTITIONS} --topic ${topic-name}

# Faust commands related
start-app:
	./scripts/run

send-page-view-event:
	PYTHONPATH={{cookiecutter.project_slug}} venv/bin/faust -A app send page_views '${payload}'

list-agents:
	PYTHONPATH={{cookiecutter.project_slug}} venv/bin/faust -A app agents

# Build docker image
build:
	docker build -t {{cookiecutter.project_slug}} .

run:
	docker run {{cookiecutter.project_slug}}
