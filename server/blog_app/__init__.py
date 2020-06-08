import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL'],
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        USER_APP_NAME='simpleBlog',
        USER_ENABLE_EMAIL=True,
        USER_ENABLE_USERNAME=False,
        USER_EMAIL_SENDER_NAME='simpleBlog',
        USER_EMAIL_SENDER_EMAIL='simleBlog@example.com'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


app = create_app()
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.teardown_request
def teardown_request(response_or_exc):
    db.session.remove()


@app.teardown_appcontext
def shutdown_session(response_or_exc):
    db.session.remove()


from blog_app import views, models, auth
