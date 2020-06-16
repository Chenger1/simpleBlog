from datetime import datetime
from flask_user import UserManager, UserMixin

from blog_app import app, db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False, server_default='')
    email = db.Column(db.String(120), unique=True, nullable=False)
    posts = db.relationship('Post')
    comments = db.relationship('Comments')

    roles = db.relationship('Role', secondary='user_roles')

    def __repr__(self):
        return f'User - {self.username}'


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_data = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)
    author = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)

    comments = db.relationship('Comments')

    def __repr__(self):
        return f'Post - {self.title}'


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(80), nullable=False)
    pub_data = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)
    author = db.Column(db.String, db.ForeignKey('users.username') ,nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    roles_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'))


user_manager = UserManager(app, db, User)

db.create_all()