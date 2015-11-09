from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from models import User
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    return User.query.get(user_id)


@app.route('/')
def index():
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
