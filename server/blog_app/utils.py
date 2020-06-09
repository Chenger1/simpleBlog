from blog_app import app, db
from blog_app.models import Post

from sqlalchemy.exc import IntegrityError


def create_post(current_user, payload):
    try:
        post = Post(
            title=payload['title'],
            user_id=current_user
        )
        db.session.add(post)
        db.session.commit()
        db.session.remove()
        response_object = {
            'status': 'success'
        }
        return response_object
    except IntegrityError as e:
        response_object = {
            'status': 'fail',
            'message': e
        }
        return response_object
