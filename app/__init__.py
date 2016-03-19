# coding: utf-8
from flask import Flask

__author__ = 'Jux.Liu'

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    from views import bp
    app.register_blueprint(bp)

    return app
