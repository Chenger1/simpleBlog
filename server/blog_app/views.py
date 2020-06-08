from blog_app import app, auth

import json
from flask import jsonify, request


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
