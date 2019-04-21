import logging

from {{cookiecutter.project_slug}}.app import app

from {{cookiecutter.project_slug}}.page_views.models import PageView

page_view_topic = app.topic("page_views", partitions=8, value_type=PageView)

page_views = app.Table("page_views", default=int)

logger = logging.getLogger(__name__)


@app.agent(page_view_topic)
async def count_page_views(views):
    async for view in views.group_by(PageView.id):
        page_views[view.id] += 1
        logger.info(f"Event received. Page view Id {view.id}")

        yield view
