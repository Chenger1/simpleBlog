import os
import tempfile

import pytest

from blog_app import create_app, app


@pytest.fixture
def client():
    db_fd, dp_path = tempfile.mkstemp()
    with app.test_client() as cl:
        yield cl
    os.close(db_fd)


def test_get(client):
    resp = client.get('/')
    assert b'Response' in resp.data