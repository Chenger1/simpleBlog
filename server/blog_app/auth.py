from blog_app import app, db
from blog_app.models import User, Role, user_manager

from flask_jwt_extended import (
    JWTManager, create_access_token,
    create_refresh_token,
)
from sqlalchemy.exc import IntegrityError

jwt = JWTManager(app)


def registration_user(payload):
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
        user.roles.append(Role.query.filter_by(name='Author').first())
        db.session.add(user)
        db.session.commit()
        db.session.remove()
        return {
            'status': 'success',
            'message': 'You have been registered'
        }
    except IntegrityError as e:
        return {
            'status': 'fail',
            'message': 'User already exists' if e.orig.pgcode == '23505' else 'Invalid Data'
        }


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user_manager.verify_password(password, user.password):
        access_token = create_access_token(identity=user.id, fresh=True)
        refresh_token = create_refresh_token(user.id)
        return {
            'id': user.id,
            'access_token': access_token,
            'refresh_token': refresh_token,
            'roles': [i.name for i in user.roles]
        }
    return {'login_status': 'Invalid data'}


@jwt.user_claims_loader
def add_claims_to_access_token(user_id):
    """
    Create a function that will be called whenever create_access_token
    is used. It will take whatever object is passed into the
    create_access_token method, and lets us define what custom claims
    should be added to the access token.
    :param user_id:
    :return: dict {'username': 'username',
                   'role': [Role1, Role2]}
    """
    user = User.query.filter_by(id=user_id).first()
    return {
        'username': user.username,
        'role': [i.name for i in user.roles]
    }
