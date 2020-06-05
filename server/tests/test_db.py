import psycopg2
from datetime import datetime

from blog_app.models import User, user_manager
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
    user = User(
        username='testing',
        email='member@example.com',
        password=user_manager.hash_password('example')
    )
    db.session.add(user)
    db.session.commit()