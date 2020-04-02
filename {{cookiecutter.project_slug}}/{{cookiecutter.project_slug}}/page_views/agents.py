import logging

from app import app

from .models import PageView

page_view_topic = app.topic("page_views", value_type=PageView)
hello_world_topic = app.topic("hello_world")

page_views = app.Table("page_views", default=int)

logger = logging.getLogger(__name__)


@app.agent(page_view_topic)
async def count_page_views(views):
    async for view in views.group_by(PageView.id):
        page_views[view.id] += 1
        logger.info(f"Event received. Page view Id {view.id}")

        yield view


@app.timer(interval=3.0)
async def producer():
    await hello_world_topic.send(key="faust", value=b'{"message": "Hello world! (Faust Version)"}')


@app.agent(hello_world_topic)
async def consumer(events):
    async for event in events:
        logger.info(event)

        yield event
