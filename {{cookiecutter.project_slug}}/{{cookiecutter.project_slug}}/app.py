import faust

from logging.config import dictConfig

from {{cookiecutter.project_slug}} import settings

conf = {
    "version": 1,  # fmt: off
    "autodiscover": True,
    "origin": "{{cookiecutter.project_slug}}",
    "id": "1",
    "broker": settings.{{cookiecutter.kafka_server_environment_variable}},
    "store": settings.STORE_URI,
    "logging_config": dictConfig(settings.LOGGING),
    "topic_allow_declare": settings.TOPIC_ALLOW_DECLARE,
    "topic_disable_leader": settings.TOPIC_DISABLE_LEADER,
}
{% if cookiecutter.include_ssl_settings.lower() == "y" %}
if settings.SSL_ENABLED:
    conf.update({
        "broker_credentials": settings.SSL_CONTEXT
    })
{% endif %}
app = faust.App(**conf)


def main() -> None:
    app.main()
