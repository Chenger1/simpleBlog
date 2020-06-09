from blog_app import app, auth
from blog_app.utils import create_post

import json
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route('/')
def main():
    return 'Response'


@app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    username = data['username']
    password = data['password']
    tokens = auth.authenticate(username, password)
    return jsonify(tokens), 200


@app.route('/create_post', methods=['POST'])
@jwt_required
def post():
    current_user = get_jwt_identity()
    data = json.loads(request.data)
    resp = create_post(current_user, data)
    return jsonify(status=resp['status']), 200
