import os
import tempfile
import pytest
import json

from blog_app import create_app, app

payload_login = {
    'username': 'testing',
    'password': 'hard_pass'
}


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
    resp = client.post('/login', data=json.dumps(payload))
    assert resp.status_code == 200


def test_create_post(client):
    payload_post = {
        'title': 'Hello',
        'body': 'How are you'
    }
    user = client.post('/login', data=json.dumps(payload_login))
    resp = client.post('/create_post',
                       data=json.dumps(payload_post),
                       headers={'Authorization':f'Bearer {user.json["access_token"]}'})
    assert resp.json['status'] == 'success'


def test_delete_post(client):
    user = client.post('/login', data=json.dumps(payload_login))
    resp = client.post('/delete_post/11',
                       headers={'Authorization':f'Bearer {user.json["access_token"]}'})
    assert resp.json['status'] == 'success'


def test_delete_post_wrong_post_id(client):
    user = client.post('/login', data=json.dumps(payload_login))
    resp = client.post('/delete_post/15',
                       headers={'Authorization': f'Bearer {user.json["access_token"]}'})
    assert resp.json['status'] == 'fail'
