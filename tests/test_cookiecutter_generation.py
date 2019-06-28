import os
import re
import sh

import pytest
from pytest_cases import pytest_fixture_plus
from binaryornot.check import is_binary

PATTERN = "{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)

YN_CHOICES = ["y", "n"]
FAUST_LOGLEVEL = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"]
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
    "include_page_view_tutorial", YN_CHOICES, ids=lambda yn: f"page_tutorial:{yn}"
)
@pytest.mark.parametrize(
    "faust_loglevel", FAUST_LOGLEVEL, ids=lambda yn: f"loglevel:{yn}"
)
@pytest.mark.parametrize("worker_port", WORKER_PORT, ids=lambda yn: f"worker_port:{yn}")
@pytest.mark.parametrize(
    "kafka_server_environment_variable",
    KAFKA_SERVER,
    ids=lambda yn: f"kafka_Server:{yn}",
)
@pytest.mark.parametrize(
    "include_codec_example", YN_CHOICES, ids=lambda yn: f"codec_example:{yn}"
)
@pytest.mark.parametrize(
    "include_schema_registry", YN_CHOICES, ids=lambda yn: f"schema_registry:{yn}"
)
@pytest.mark.parametrize(
    "include_rocksdb", YN_CHOICES, ids=lambda yn: f"rocksdb:{yn}"
)
def context_combination(
    use_docker,
    include_docker_compose,
    include_page_view_tutorial,
    faust_loglevel,
    worker_port,
    kafka_server_environment_variable,
    include_codec_example,
    include_schema_registry,
):
    """Fixture that parametrize the function where it's used."""
    return {
        "use_docker": use_docker,
        "include_docker_compose": include_docker_compose,
        "include_page_view_tutorial": include_page_view_tutorial,
        "faust_loglevel": faust_loglevel,
        "worker_port": worker_port,
        "kafka_server_environment_variable": kafka_server_environment_variable,
        "include_codec_example": include_codec_example,
        "include_schema_registry": include_schema_registry,
        "include_rocksdb": include_rocksdb,
    }


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    """Method to check all paths have correct substitutions,
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
    This is parametrized for each combination from ``context_combination`` fixture
    """
    result = cookies.bake(extra_context={**context, **context_combination})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["project_slug"]
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)


# def test_linting_passes(cookies, context_combination):
#     """
#     Generated project should pass flake8 & black.
#     This is parametrized for each combination from ``context_combination`` fixture
#     """
#     result = cookies.bake(extra_context=context_combination)

#     try:
#         sh.flake8(str(result.project))
#     except sh.ErrorReturnCode as e:
#         pytest.fail(e)

#     try:
#         sh.black("--check", "--diff", f"{result.project}/")
#     except sh.ErrorReturnCode as e:
#         pytest.fail(e)
