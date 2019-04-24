from pathlib import Path
from setuptools import setup, find_packages
from typing import List


def parse_requirements(filename: str) -> List[str]:
    """Return requirements from requirements file."""
    # Ref: https://stackoverflow.com/a/42033122/
    requirements = (Path(__file__).parent / filename).read_text().strip().split('\n')
    requirements = [r.strip() for r in requirements]
    requirements = [r for r in sorted(requirements) if r and not r.startswith('#')]
    return requirements


setup(
    name="{{cookiecutter.project_name}}",
    version="{{cookiecutter.version}}",
    description="{{cookiecutter.description}}",
    long_description="""{{cookiecutter.description}}""",
    classifiers=["Programming Language :: Python"],
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    url="https://github.com/marcosschroh/cookiecutter-faust",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=parse_requirements("requirements.txt"),
    tests_require=[],
    setup_requires=[],
    dependency_links=[],
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_slug}} = {{cookiecutter.project_slug}}.app:main"
        ],
        {% if cookiecutter.include_codec_example == "y" %}
        "faust.codecs": [
            "msgpack_codec = {{cookiecutter.project_slug}}.codecs.codec:msgpack",
            # add entries here to add more custom codecs
        ],
        {% endif %}
    },
)
