from blog_app import app
from blog_app.models import User, user_manager

from flask_jwt_extended import (
    JWTManager, create_access_token,
    create_refresh_token,
)

jwt = JWTManager(app)


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