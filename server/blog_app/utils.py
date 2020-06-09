from blog_app import app, db
from blog_app.models import Post

from sqlalchemy.exc import IntegrityError


def create_post(current_user, payload):
    try:
        post = Post(
            title=payload['title'],
            body=payload['body'],
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


def delete_post(post_id, user_id):
    try:
        post = Post.query.filter_by(id=post_id).first()
        if post.user_id == user_id:
            db.session.delete(post)
            db.session.commit()
            db.session.remove()
            response_object = {
                'status': 'success',
            }
            return response_object
    except AttributeError as e:
        response_object = {
            'status': 'fail',
        }
        return response_object
