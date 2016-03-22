# coding: utf-8
import json

from app.main.models import LoginForm
from app.user.models import User
from flask import render_template, request, redirect, url_for, send_from_directory, session
from flask.ext.login import current_user, logout_user, login_user
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
    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        u = User.query.filter_by(username=username).first()
        if u.verify_password(password=password):
            login_user(u)
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            return json.dumps({'code': 2, 'msg': 'Username/Password Error'})
    return render_template("login.html", form=login_form)


@main.route('/logout/')
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('main.login'))
