from blog_app import app, db
from blog_app.models import User, user_manager

from flask_jwt_extended import (
    JWTManager, create_access_token,
    create_refresh_token,
)
from sqlalchemy.exc import IntegrityError

jwt = JWTManager(app)


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
            'access_token': access_token,
            'refresh_token': refresh_token,
        }
    return {'login_status': 'Invalid data'}