import os
import re

import pytest
from binaryornot.check import is_binary
from pytest_cases import pytest_fixture_plus

PATTERN = "{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)

YN_CHOICES = ["y", "n"]
log_level = ["CRITICAL", "ERROR", ]
CI_PROVIDERS = ["travis", "gitlab", "none", ]
WORKER_PORT = [6066, 8000, 8080]
KAFKA_SERVER = ["KAFKA_BOOTSTRAP_SERVER", "KAFKA_SERVER"]


@pytest.fixture
def context():
    return {
        "project_name": "My Awesome Faust Project",
        "project_slug": "my_awesome_faust_project",
        "author_name": "Test Author",
        "email": "test@example.com",
        "description": "My Awesome Faust Project!",
        "version": "0.1.0",
    }


@pytest_fixture_plus
@pytest.mark.parametrize("use_docker", YN_CHOICES, ids=lambda yn: f"docker:{yn}")
@pytest.mark.parametrize(
    "include_docker_compose", YN_CHOICES, ids=lambda yn: f"docker_compose:{yn}"
)
@pytest.mark.parametrize(
    "log_level", log_level, ids=["CRITICAL", "ERROR", ]
)
@pytest.mark.parametrize("worker_port", WORKER_PORT, ids=lambda yn: f"worker_port:{yn}")
@pytest.mark.parametrize(
    "include_schema_registry", YN_CHOICES, ids=lambda yn: f"schema_registry:{yn}"
)
@pytest.mark.parametrize("include_rocksdb", YN_CHOICES, ids=lambda yn: f"rocksdb:{yn}")
@pytest.mark.parametrize(
    "ci_provider", CI_PROVIDERS, ids=["travis", "gitlab", "none", ]
)
def context_combination(
    use_docker,
    include_docker_compose,
    log_level,
    worker_port,
    include_schema_registry,
    include_rocksdb,
    ci_provider,
):
    """Fixture that parametrize the function where it's used."""
    return {
        "use_docker": use_docker,
        "include_docker_compose": include_docker_compose,
        "log_level": log_level,
        "worker_port": worker_port,
        "include_schema_registry": include_schema_registry,
        "include_rocksdb": include_rocksdb,
        "ci_provider": ci_provider,
    }


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    """
    Method to check all paths have correct substitutions,
    used by other tests cases
    """
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue

        for line in open(path, "r"):
            match = RE_OBJ.search(line)
            msg = "cookiecutter variable not replaced in {}"
            assert match is None, msg.format(path)


def test_project_generation(cookies, context, context_combination):
    """
    Test that project is generated and fully rendered.
    This is parametrized for each combination from ``context_combination``
    fixture
    """
    result = cookies.bake(extra_context={**context, **context_combination})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["project_slug"]
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)
