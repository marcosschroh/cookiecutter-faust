#!/bin/bash
set -x

export SIMPLE_SETTINGS={{cookiecutter.project_slug}}.settings

# Install the application. The Dockerfile build installs everything in
# requirements.txt so this will only install the application and any
# dependencies added since the image was last built.
pip3 install -e /repo_root_mount

# Run the application with exec, replacing this shell script in the same
# process. Exec is used so dumb-init can easily forward signals to the
# application.
exec {{cookiecutter.project_slug}} worker --web-port={% if cookiecutter.include_docker_compose %}$WORKER_PORT{% else %}{{cookiecutter.worker_port}}{% endif %}
