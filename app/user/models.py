# coding: utf-8
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

__author__ = 'Jux.Liu'


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password = db.Column('password', db.String(120), nullable=False)

    def __repr__(self):
        return '<User #{0}: {1}, email: {2}>'.format(self.id, self.username, self.email)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password = generate_password_hash(password=password)

    def verify_password(self, password):
        if self.password is None or password is None:
            return False
        return check_password_hash(self.password, password)

    def generate(self):
        self.save()
        return self

    @staticmethod
    @login_manager.user_loader
    def get_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def is_exists(column, value):
        return db.session.query(db.exists().where(column == value)).scalar()
