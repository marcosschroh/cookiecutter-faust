import pytest

from {{cookiecutter.project_slug}}.page_views.models import PageView
from {{cookiecutter.project_slug}}.page_views.agents import count_page_views, page_views
from {{cookiecutter.project_slug}}.app import app


@pytest.fixture()
def test_app(event_loop):
    """passing in event_loop helps avoid 'attached to a different loop' error"""
    app.finalize()
    app.conf.store = 'memory://'
    app.flow_control.resume()
    return app


@pytest.mark.asyncio()
async def test_count_page_views(test_app):
    async with count_page_views.test_context() as agent:
        page_view = PageView(id='1', user='test')
        page_view_2 = PageView(id='1', user='test2')
        await agent.put(page_view)

        # windowed table: we select window relative to the current event
        assert page_views['1'] == 1

        await agent.put(page_view_2)
        assert page_views['1'] == 2
