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


# def test_auth(client):
#     payload = {
#         'username': 'testing',
#         'password': 'hard_pass'
#     }
#     resp = client.post('/login', data=json.dumps(payload))
#     assert resp.status_code == 200


def test_post(client):
    payload_login = {
        'username': 'testing',
        'password': 'hard_pass'
    }
    payload_post = {
        'title': 'Hello',
        'body': 'How are you'
    }
    user = client.post('/login', data=json.dumps(payload_login))
    resp = client.post('/create_post',
                       data=json.dumps(payload_post),
                       headers={'Authorization':f'Bearer {user.json["access_token"]}'})
    assert resp.json['status'] == 'success'
