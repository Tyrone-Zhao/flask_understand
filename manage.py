from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from deep_understand_flask import create_app
from deep_understand_flask.models import db, User, Post, Tag, Comment
import os


# 默认使用dev配置
env = os.environ.get("DEEP_UNDERSTAND_FLASK_ENV", "dev")
app = create_app("deep_understand_flask.config.%sConfig" % env.capitalize())

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User,
        Post=Post,
        Tag=Tag,
        Comment=Comment
    )

if __name__ == "__main__":
    manager.run()
