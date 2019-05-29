from setuptools import setup, find_packages

requires = [
    "avro-python3",
    "colorlog==3.1.4",
    "fastavro",
    "faust==1.5.4",
    "robinhood-aiokafka==1.0.2",
    "requests",
    "simple-settings==0.16.0",
    {% if cookiecutter.include_codec_example.lower() == "y" %}
    "msgpack==0.6.1",{% endif %}
    {% if cookiecutter.include_schema_registry.lower() == "y" %}
    "python-schema-registry-client",{% endif %}
]

setup(
    name="{{cookiecutter.project_name}}",
    version="{{cookiecutter.version}}",
    description="{{cookiecutter.description}}",
    long_description="""{{cookiecutter.description}}""",
    classifiers=["Programming Language :: Python"],
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    url="",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=[],
    setup_requires=[],
    dependency_links=[],
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_slug}} = {{cookiecutter.project_slug}}.app:main"
        ],
        {% if cookiecutter.include_codec_example.lower() == "y" %}
        "faust.codecs": [
            "msgpack_codec = {{cookiecutter.project_slug}}.codecs.codec:msgpack",
            # add entries here to add more custom codecs
        ],
        {% endif %}
    },
)
