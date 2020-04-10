import faust

from simple_settings import settings

app = faust.App(
    id=1,
    debug=settings.DEBUG,
    autodiscover=["page_views"],
    broker=settings.KAFKA_BOOTSTRAP_SERVER,
    store=settings.STORE_URI,
    logging_config=settings.LOGGING,
    topic_allow_declare=settings.TOPIC_ALLOW_DECLARE,
    topic_disable_leader=settings.TOPIC_DISABLE_LEADER,
    broker_credentials=settings.SSL_CONTEXT,
)
