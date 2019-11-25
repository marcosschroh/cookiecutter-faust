#!/bin/sh -e

export PREFIX=""
if [ -d 'venv' ] ; then
    export PREFIX="venv/bin/"
fi

export VERSION_SCRIPT="import sys; print('%s.%s' % sys.version_info[0:2])"
export PYTHON_VERSION=`python -c "$VERSION_SCRIPT"`
export SIMPLE_SETTINGS="{{cookiecutter.project_slug}}.settings"

set -x

PYTHONPATH=. ${PREFIX}pytest ${1-"./tests"}
