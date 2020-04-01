import pytest

from page_views.agents import count_page_views, page_views
from page_views.models import PageView


@pytest.mark.asyncio()
async def test_count_page_views(test_app):
    async with count_page_views.test_context() as agent:
        page_view = PageView(id="1", user="test")
        page_view_2 = PageView(id="1", user="test2")
        await agent.put(page_view)

        # windowed table: we select window relative to the current event
        assert page_views["1"] == 1

        await agent.put(page_view_2)
        assert page_views["1"] == 2
