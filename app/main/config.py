# coding: utf-8
from os import environ
from os.path import abspath, dirname, join

__author__ = 'Jux.Liu'


class Config():
    SECRET_KEY = environ.get('SECRET_KEY') or 'the answer of life, universe and everything'
    FLASKY_ADMIN = environ.get('FLASKY_ADMIN')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    WTF_CSRF_ENABLED = True
    WTF_CSRF_METHODS = ['POST', 'PUT', 'DELETE', 'PATCH']

    @staticmethod
    def init_app(app):
        # configure_errorhandlers(app)
        # blueprint.regist(app)
        # signals.regist(app)
        # whooshalchemy.regist(app)
        # create_admin(app)
        pass


basedir = abspath(dirname(__file__))


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or 'sqlite:////home/jux/Documents/qblog/data.sqlite'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URL') or 'sqlite:////home/jux/Documents/qblog/data-dev.sqlite'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('TEST_DATABASE_URL') or 'sqlite:////home/jux/Documents/qblog/data-test.sqlite'


config = {
    'default': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'develop': DevelopmentConfig
}
