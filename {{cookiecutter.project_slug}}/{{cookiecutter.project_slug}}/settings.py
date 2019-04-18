SIMPLE_SETTINGS = {
    'OVERRIDE_BY_ENV': True,
    'CONFIGURE_LOGGING': True,
    'REQUIRED_SETTINGS': ('{{cookiecutter.kafka_server_environment_variable}}',),
}

# The following variables can be ovirriden from ENV
{{cookiecutter.kafka_server_environment_variable}} = "kafka://kafka:9092"
# SCHEMA_REGISTRY_URL = "http://schema-registry:8081"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': '{{cookiecutter.faust_loglevel}}',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        '{{cookiecutter.project_slug}}': {
            'handlers': ['console'],
            'level': '{{cookiecutter.faust_loglevel}}',
        },
    },
}
