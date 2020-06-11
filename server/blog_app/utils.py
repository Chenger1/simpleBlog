from blog_app import app, db
from blog_app.models import User, Post, Comments

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
        return {'status': 'success'}
    except IntegrityError as e:
        return {'status': 'fail', 'message': e}


def delete_post(post_id, user_id):
    try:
        post = Post.query.filter_by(id=post_id).first()
        if post.user_id == user_id:
            post_comments = Comments.__table__.delete().where(
                Comments.post_id == post_id
            )
            db.session.execute(post_comments)
            db.session.delete(post)
            db.session.commit()
            db.session.remove()
            return {'status': 'success'}
    except AttributeError as e:
        return {'status': 'fail', 'message': e}


def edit_post(post_id, user_id, payload):
    try:
        post = Post.query.filter_by(id=post_id).first()
        if post.user_id == user_id:
            if payload['title'] != post.title: post.title = payload['title']
            if payload['body'] != post.body: post.body = payload['body']
            db.session.add(post)
            db.session.commit()
            db.session.remove()
            return {'status': 'success'}
        return {'status': 'fail'}
    except AttributeError as e:
        return {'status': 'fail'}


def create_comment(post_id, user_id, payload):
    try:
        comment = Comments(
            body=payload['body'],
            user_id=user_id,
            post_id=post_id
        )
        db.session.add(comment)
        db.session.commit()
        db.session.remove()
        return {'status': 'success'}
    except IntegrityError as e:
        return {'status': 'fail',
                'message': e}


def edit_comment(comment_id, user_id, payload):
    try:
        comment = Comments.query.filter_by(id=comment_id).first()
        if comment.user_id == user_id:
            if payload['body'] != comment.body: comment.body = payload['body']
            db.session.add(comment)
            db.session.commit()
            db.session.remove()
            return {'status': 'success'}
        return {'status': 'fail'}
    except AttributeError as e:
        return {'status': 'fail'}


def delete_comment(comment_id, user_id):
    try:
        comment = Comments.query.filter_by(id=comment_id).first()
        if comment.user_id == user_id:
            db.session.delete(comment)
            db.session.commit()
            db.session.remove()
            return {'status': 'success'}
        return {'status': 'fail'}
    except AttributeError as e:
        return {'status': 'fail'}


def user_info(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()
        breakpoint()
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'posts': [{
                'id': post.id,
                'title': post.title,
                'body': post.body,
                'pub_data': post.pub_data
            } for post in user.posts],
            'comments': [{
                'id': comment.id,
                'body': comment.body,
                'post_id': comment.post_id,
                'pub_data': comment.pub_data
            } for comment in user.comments]
        }
    except Exception as e:
        return {
            'message': e
        }
