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
    resp = client.post('/login', data=json.dumps(payload_login))
    assert resp.status_code == 200


def test_create_post(client):
    payload_post = {
        'title': 'Tested',
        'body': 'How are you'
    }
    user = client.post('/login', data=json.dumps(payload_login))
    resp = client.post('/create_post',
                       data=json.dumps(payload_post),
                       headers={'Authorization': f'Bearer {user.json["access_token"]}'})
    assert resp.json['status'] == 'success'


def test_delete_post(client):
    user = client.post('/login', data=json.dumps(payload_login))
    resp = client.post('/delete_post/16',
                       headers={'Authorization':f'Bearer {user.json["access_token"]}'})
    assert resp.json['status'] == 'success'


def test_delete_post_wrong_post_id(client):
    user = client.post('/login', data=json.dumps(payload_login))
    resp = client.post('/delete_post/15',
                       headers={'Authorization': f'Bearer {user.json["access_token"]}'})
    assert resp.json['status'] == 'fail'


def test_edit_post(client):
    payload_post = {
        'title': 'Edited',
        'body': 'How are you'
    }
    user = client.post('/login', data=json.dumps(payload_login))
    resp = client.post('/edit_post/2',
                       data=json.dumps(payload_post),
                       headers={'Authorization': f'Bearer {user.json["access_token"]}'})
    assert resp.json['status'] == 'success'


def test_create_comments(client):
    payload_comment = {
        'body': 'second comment'
    }
    user = client.post('/login', data=json.dumps(payload_login))
    resp = client.post('/create_comment/14',
                       data=json.dumps(payload_comment),
                       headers={'Authorization': f'Bearer {user.json["access_token"]}'})
    assert resp.json['status'] == 'success'


def test_edit_comments(client):
    payload_comment = {
        'body': 'Edited'
    }
    user = client.post('/login', data=json.dumps(payload_login))
    resp = client.post('/edit_comment/3',
                       data=json.dumps(payload_comment),
                       headers={'Authorization': f'Bearer {user.json["access_token"]}'})
    assert resp.json['status'] == 'success'


def test_delete_comment(client):
    user = client.post('/login', data=json.dumps(payload_login))
    resp = client.post('/delete_comment/3',
                       headers={'Authorization': f'Bearer {user.json["access_token"]}'})
    assert resp.json['status'] == 'success'


def test_user_info(client):
    user = client.post('/login', data=json.dumps(payload_login))
    resp = client.post('/user_info/35',
                       headers={'Authorization': f'Bearer {user.json["access_token"]}'})
    assert resp.json['email'] == 'member@gmail.com'
    assert resp.json['username'] == 'testing'
    assert resp.json['posts'][0]['title'] == 'Hello'


def test_admin_page(client):
    payload_admin = {
        'username': 'some_admin',
        'password': 'admin_pass'
    }
    user = client.post('/login', data=json.dumps(payload_login))
    resp = client.post('/admin_page',
                       headers={'Authorization': f'Bearer {user.json["access_token"]}'})
    assert resp.json['current_identity'] == 36
