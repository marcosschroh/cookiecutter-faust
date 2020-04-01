import pytest

from app import app


@pytest.fixture()
def test_app(event_loop):
    """passing in event_loop helps avoid 'attached to a different loop' error"""
    app.finalize()
    app.conf.store = "memory://"
    app.flow_control.resume()
    return app
