#!/bin/sh
# sh tests/test_docker.sh

set -o errexit
project_name="my_awesome_faust_project"

# install test requirements
pip install faust==1.9.0 simple-settings==0.16.0
pip install -r ./requirements.txt

# create a cache directory
mkdir -p .cache/docker
cd .cache/docker

# create the project using the default settings in cookiecutter.json
cookiecutter ../../ --no-input --overwrite-if-exists $@
cd ${project_name}

docker-compose stop
echo yes | docker-compose rm
docker network rm ${project_name} | true

./scripts/test.sh

docker-compose run -e SIMPLE_SETTINGS=${project_name}.settings ${project_name} echo "project running... :-)"
