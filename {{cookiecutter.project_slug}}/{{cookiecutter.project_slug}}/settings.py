import ssl
from logging.config import dictConfig

DEBUG = True

SIMPLE_SETTINGS = {
    "OVERRIDE_BY_ENV": True,
    "CONFIGURE_LOGGING": True,
    "REQUIRED_SETTINGS": ("KAFKA_BOOTSTRAP_SERVER", "STORE_URI"),
}

KAFKA_BOOTSTRAP_SERVER = "kafka://localhost:29092"
# SCHEMA_REGISTRY_URL = "http://schema-registry:8081"

# Faust storage
STORE_URI = "memory://"

LOGGING = dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {"default": {"format": "%(asctime)s %(levelname)s %(name)s %(message)s"}},
        "handlers": {
            "console": {
                "level": "{{cookiecutter.log_level}}",
                "class": "logging.StreamHandler",
                "formatter": "default",
            }
        },
        "loggers": {"page_views": {"handlers": ["console"], "level": "{{cookiecutter.log_level}}"}},
    }
)

TOPIC_ALLOW_DECLARE = True
TOPIC_DISABLE_LEADER = False

SSL_ENABLED = False
SSL_CONTEXT = None

if SSL_ENABLED:
    # file in pem format containing the client certificate, as well as any ca certificates
    # needed to establish the certificate’s authenticity
    KAFKA_SSL_CERT = None

    # filename containing the client private key
    KAFKA_SSL_KEY = None

    # filename of ca file to use in certificate verification
    KAFKA_SSL_CABUNDLE = None

    # password for decrypting the client private key
    SSL_KEY_PASSWORD = None

    SSL_CONTEXT = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=KAFKA_SSL_CABUNDLE)

    SSL_CONTEXT.load_cert_chain(KAFKA_SSL_CERT, keyfile=KAFKA_SSL_KEY, password=SSL_KEY_PASSWORD)
