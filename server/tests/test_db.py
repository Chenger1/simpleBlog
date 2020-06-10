import psycopg2
from datetime import datetime

from blog_app.models import User, Role, user_manager
from blog_app import db


def test_db():
    conn = psycopg2.connect(
            host="localhost",
            database="blog_db",
            user="test",
            password="test"
        )
    cur = conn.cursor()
    cur.execute('SELECT version()')

    db_version = cur.fetchone()
    cur.close()
    conn.close()


def test_user_create_without_roles():
    payload = {
        'username': 'testing',
        'email': 'member@gmail.com',
        'password': 'hard_pass'
    }
    resp = User.registration(payload)
    assert resp['status'] == 'success'
    assert resp['message'] == 'You have been registered'


def test_user_create_with_roles():
    user = User(
        username='some_admin',
        email='admin@example.com',
        password=user_manager.hash_password('admin_pass')
    )
    user.roles.append(Role(name='Admin'))
    user.roles.append(Role(name='Author'))
    db.session.add(user)
    db.session.commit()
    db.session.remove()