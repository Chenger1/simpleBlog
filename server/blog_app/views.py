from blog_app import app
from blog_app.auth import authenticate, registration_user
from blog_app.utils import (main_page,
                            create_post, delete_post, edit_post,
                            create_comment, edit_comment, delete_comment,
                            user_info
                            )

import json
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims


@app.route('/')
def main():
    resp = main_page()
    return jsonify(resp=resp), 200


@app.route('/registration', methods=['POST'])
def registration():
    data = json.loads(request.data)
    user = registration_user(data)
    return jsonify(user), 201


@app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    username = data['username']
    password = data['password']
    tokens = authenticate(username, password)
    return jsonify(tokens), 200 if 'access_token' in tokens.keys() else 400


@app.route('/create_post', methods=['POST'])
@jwt_required
def crt_post():
    current_user = get_jwt_identity()
    data = json.loads(request.data)
    resp = create_post(data)
    return jsonify(status=resp['status']), 201


@app.route('/delete_post/<post_id>', methods=['POST'])
@jwt_required
def del_post(post_id=None):
    current_user = get_jwt_identity()
    data = json.loads(request.data)
    resp = delete_post(post_id, current_user, data['username'])
    return jsonify(status=resp['status']), 200


@app.route('/edit_post/<post_id>', methods=['PATCH'])
@jwt_required
def ed_post(post_id=None):
    current_user = get_jwt_identity()
    data = json.loads(request.data)
    resp = edit_post(post_id, current_user, data)
    return jsonify(status=resp['status']), 200


@app.route('/create_comment/<post_id>', methods=['POST'])
@jwt_required
def crt_comment(post_id=None):
    current_user = get_jwt_identity()
    data = json.loads(request.data)
    resp = create_comment(post_id, data)
    return jsonify(status=resp['status']), 201


@app.route('/edit_comment/<comment_id>', methods=['PATCH'])
@jwt_required
def ed_comment(comment_id=None):
    current_user = get_jwt_identity()
    data = json.loads(request.data)
    resp = edit_comment(comment_id,current_user, data)
    return jsonify(status=resp['status']), 200


@app.route('/delete_comment/<comment_id>', methods=['POST'])
@jwt_required
def del_comment(comment_id=None):
    current_user = get_jwt_identity()
    data = json.loads(request.data)
    resp = delete_comment(comment_id, current_user, data['username'])
    return jsonify(status=resp['status']), 200


@app.route('/user_info/<username>', methods=['GET'])
def us_info(username=None):
    current_user = get_jwt_identity()
    resp = user_info(username)
    return jsonify(id=resp['id'],
                   username=resp['username'],
                   email=resp['email'],
                   posts=resp['posts'],
                   comments=resp['comments']
                   ), 200


@app.route('/admin_page', methods=['POST'])
@jwt_required
def admin():
    current_user = {
        'current_identity': get_jwt_identity(),
        'current_roles': get_jwt_claims()
    }
    if 'Admin' in current_user['current_roles']['role']:
        return jsonify(current_user), 200
    else:
        return jsonify('Fail'), 200

