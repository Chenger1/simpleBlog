import os
import tempfile
import pytest
import json

from blog_app import create_app, app



@pytest.fixture
def client():
    db_fd, dp_path = tempfile.mkstemp()
    app.config['TESTING'] = True
    with app.test_client() as cl:
        with app.app_context():
            yield cl
    os.close(db_fd)


def test_get(client):
    resp = client.get('/')
    assert b'Response' in resp.data


def test_auth(client):
    payload = {
        'username': 'testing',
        'password': 'hard_pass'
    }
    resp = client.post('/login', data=json.dumps(payload))
    assert resp.status_code == 200