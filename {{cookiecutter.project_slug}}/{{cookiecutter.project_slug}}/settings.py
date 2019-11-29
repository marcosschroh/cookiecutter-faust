import os
{% if cookiecutter.include_ssl_settings.lower() == "y" %}
import ssl
{% endif %}
SIMPLE_SETTINGS = {
    "OVERRIDE_BY_ENV": True,
    "CONFIGURE_LOGGING": True,
    "REQUIRED_SETTINGS": ("{{cookiecutter.kafka_server_environment_variable}}",),
}

# The following variables can be ovirriden from ENV
{{cookiecutter.kafka_server_environment_variable}} = "kafka://kafka:9092"
# SCHEMA_REGISTRY_URL = "http://schema-registry:8081"
{% if cookiecutter.include_rocksdb.lower() == "y" %}
STORE_URI = "rocksdb://"
{% else %}
STORE_URI = "memory://"
{% endif %}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {"format": "%(asctime)s %(levelname)s %(name)s %(message)s"}
    },
    "handlers": {
        "console": {
            "level": "{{cookiecutter.faust_loglevel}}",
            "class": "logging.StreamHandler",
            "formatter": "default",
        }
    },
    "loggers": {  # fmt: off
        "{{cookiecutter.project_slug}}": {
            "handlers": ["console"],
            "level": "{{cookiecutter.faust_loglevel}}",
        }
    },
}

TOPIC_ALLOW_DECLARE = os.getenv("TOPIC_ALLOW_DECLARE", True)
TOPIC_DISABLE_LEADER = os.getenv("TOPIC_DISABLE_LEADER", False)
{% if cookiecutter.include_ssl_settings.lower() == "y" %}
SSL_ENABLED = os.getenv("SSL_ENABLED", False)

if SSL_ENABLED:
    # file in pem format containing the client certificate, as well as any ca certificates
    # needed to establish the certificate’s authenticity
    SSL_CERT_FILE = "path_to_ssl_certificate.pem"

    # filename containing the client private key
    SSL_KEY_FILE = "path_tp_private_key.key"

    # filename of ca file to use in certificate verification
    CA_FILE = "path_to_ca_file.crt"

    # password for decrypting the client private key
    SSL_KEY_PASSWORD = os.getenv("SSL_KEY_PASSWORD")

    SSL_CONTEXT = ssl.create_default_context(
        purpose=ssl.Purpose.SERVER_AUTH, cafile=CA_FILE)
    SSL_CONTEXT.load_cert_chain(SSL_CERT_FILE, keyfile=SSL_KEY_FILE, password=SSL_KEY_PASSWORD)
{% endif %}
