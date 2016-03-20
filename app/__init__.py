# coding: utf-8
from config import config
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

__author__ = 'Jux.Liu'

db = SQLAlchemy()
login_manager=LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app=app)
    db.init_app(app=app)

    from .main import main
    app.register_blueprint(main)

    return app
