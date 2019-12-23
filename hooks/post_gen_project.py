import os
import shutil


def remove_files(file_names):
    for file_name in file_names:
        os.remove(file_name)


def remove_page_view_tutorial():
    shutil.rmtree("{{cookiecutter.project_slug}}/page_views")
    os.remove("tests/test_page_views.py")


def remove_codec():
    shutil.rmtree("{{cookiecutter.project_slug}}/codecs")


def clean_ci_providers(ci_option):
    CI_OPTIONS = {
        "travis": ".travis.yml",
    }

    if ci_option != "none":
        CI_OPTIONS.pop(ci_option)

    remove_files(CI_OPTIONS.values())


def main():
    docker_files = []
    if "{{ cookiecutter.include_docker_compose }}".lower() == "n":
        docker_files = ["docker-compose.yaml", "wait_for_services.sh", "Makefile"]

    if "{{ cookiecutter.use_docker }}".lower() == "n":
        docker_files.extend(["Dockerfile", ".dockerignore"])

    remove_files(docker_files)
    clean_ci_providers("{{ cookiecutter.ci_provider }}".lower())

    if "{{ cookiecutter.include_page_view_tutorial }}".lower() == "n":
        remove_page_view_tutorial()

    if "{{ cookiecutter.include_codec_example }}".lower() == "n":
        remove_codec()


if __name__ == "__main__":
    main()
