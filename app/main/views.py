# coding: utf-8
import json

from app.user.models import User
from flask import render_template, request, redirect, url_for, send_from_directory, session
from flask.ext.login import current_user, logout_user
from . import main

__author__ = 'Jux.Liu'


@main.route('/')
@main.route('/index')
def index():
    if current_user.is_authenticated:
        pass
    return render_template('index.html')


@main.route('/favicon.ico')
def favicon():
    """
站点图标设置
    :param: null
    :return:
    """
    return send_from_directory('static/images', 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@main.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        username = request.get_json()['username']
        password = request.get_json()['password']
        u = User.query.filter_by(username=username).first()
        if u.verify_password(password=password):
            session[u.id] = u
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            return json.dumps({'code': 2, 'msg': 'Username/Password Error'})
    return render_template("login.html")


@main.route('/logout/<int:user_id>')
def logout(user_id):
    logout_user()
    session[user_id] = None
    return redirect(url_for('main.login'))
