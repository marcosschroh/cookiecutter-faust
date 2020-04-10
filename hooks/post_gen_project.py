import os


def remove_files(file_names):
    for file_name in file_names:
        os.remove(file_name)


def clean_ci_providers(ci_option):
    CI_OPTIONS = {
        "travis": ".travis.yml",
        "gitlab": ".gitlab-ci.yml",
    }

    if ci_option != "none":
        CI_OPTIONS.pop(ci_option)

    remove_files(CI_OPTIONS.values())


def main():
    clean_ci_providers("{{ cookiecutter.ci_provider }}".lower())


if __name__ == "__main__":
    main()
