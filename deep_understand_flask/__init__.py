from flask import Flask, redirect, url_for
from deep_understand_flask.models import db
from deep_understand_flask.controllers.blog import blog_blueprint
from deep_understand_flask.extensions import bcrypt


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)
    bcrypt.init_app(app)

    @app.route('/')
    def index():
        return redirect(url_for('blog.home'))

    app.register_blueprint(blog_blueprint)

    return app
