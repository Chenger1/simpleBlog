from datetime import datetime
from flask_user import UserManager, UserMixin
from sqlalchemy.exc import IntegrityError

from blog_app import app, db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False, server_default='')
    email = db.Column(db.String(120), unique=True, nullable=False)
    posts = db.relationship('Post')

    roles = db.relationship('Role', secondary='user_roles')

    def __repr__(self):
        return f'User - {self.username}'

    @staticmethod
    def registration(payload):
        """
        e.orig.pgcode=='23505' -- UniqueViolation Error
        :param payload:
        :return:    {
                        'status': 'success' or 'fail',
                        'message': 'Some message'
                    }
        """
        try:
            user = User(
                username=payload['username'],
                email=payload['email'],
                password=user_manager.hash_password(payload['password'])
            )
            db.session.add(user)
            db.session.commit()
            db.session.remove()
            responseObject = {
                'status': 'success',
                'message': 'You have been registered'
            }
            return responseObject
        except IntegrityError as e:
            responseObject = {
                'status': 'fail',
                'message': 'User already exists' if e.orig.pgcode=='23505' else 'Invalid Data'
            }
            return responseObject


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_data = db.Column(db.DateTime, nullable=False,
                         default= datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'Post - {self.title}'


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