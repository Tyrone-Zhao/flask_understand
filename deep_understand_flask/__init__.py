from flask import Flask, redirect, url_for
from deep_understand_flask.config import DevConfig

from deep_understand_flask.models import db
from deep_understand_flask.controllers.blog import blog_blueprint


app = Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)


@app.route('/')
def index():
    return redirect(url_for('blog.home'))

app.register_blueprint(blog_blueprint)


if __name__ == '__main__':
    app.run()
