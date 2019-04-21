import os
import shutil


def remove_docker_files(file_names):
    for file_name in file_names:
        os.remove(file_name)


def remove_page_view_tutorial():
    shutil.rmtree("{{cookiecutter.project_slug}}/page_views")
    os.remove("tests/test_page_views.py")


def main():

    docker_files = []
    if "{{ cookiecutter.include_docker_compose }}".lower() == "n":
        docker_files = ["docker-compose.yaml", "wait_for_services.sh", "Makefile"]

    if "{{ cookiecutter.use_docker }}".lower() == "n":
        docker_files.extend(["Dockerfile", ".dockerignore"])

    remove_docker_files(docker_files)

    if "{{ cookiecutter.include_page_view_tutorial }}".lower() == "n":
        remove_page_view_tutorial()


if __name__ == "__main__":
    main()
