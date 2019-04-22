#!/bin/sh
# sh tests/test_docker.sh

set -o errexit

# install test requirements
pip install cookiecutter==1.6.0

# create a cache directory
mkdir -p .cache/docker
cd .cache/docker

# create the project using the default settings in cookiecutter.json
cookiecutter ../../ --no-input --overwrite-if-exists $@
cd my_awesome_faust_project

# run the project's. Install tox and run the tests.
docker-compose run -e SIMPLE_SETTINGS=my_awesome_faust_project.settings my_awesome_faust_project pip install tox; tox
