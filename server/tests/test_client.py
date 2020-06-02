import os
import tempfile

import pytest

from blog_app import create_app


@pytest.fixture
def client():
    """"
    Create and configure a new app instance for each test.
    """
    db_fd, dp_path = tempfile.mkstemp()
    app = create_app({'TESTING':True})

    with app.test_client() as client:
        yield client

    os.close(db_fd)


def test_get(client):
    resp = client.get('/')
    assert b'Response' in resp.data