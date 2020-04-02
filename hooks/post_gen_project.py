import os


def remove_files(file_names):
    for file_name in file_names:
        os.remove(file_name)


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
        docker_files = ["docker-compose.yaml", "scripts/wait-for-services", "Makefile"]

    if "{{ cookiecutter.use_docker }}".lower() == "n":
        docker_files.extend(["Dockerfile", ".dockerignore"])

    remove_files(docker_files)
    clean_ci_providers("{{ cookiecutter.ci_provider }}".lower())


if __name__ == "__main__":
    main()
