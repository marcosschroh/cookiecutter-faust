import faust

from simple_settings import settings
from logging.config import dictConfig


app = faust.App(
    version=1,  # fmt: off
    autodiscover=True,
    origin="{{cookiecutter.project_slug}}",
    id="1",
    broker=settings.{{cookiecutter.kafka_server_environment_variable}},
    logging_config=dictConfig(settings.LOGGING),
)


def main() -> None:
    app.main()
