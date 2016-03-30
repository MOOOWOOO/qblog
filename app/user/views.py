# coding: utf-8
from app.main.decorator import login_required_
from flask import render_template, g
from . import user
from .models import User

__author__ = 'Jux.Liu'


@user.route('/about/', methods=['GET', 'POST'])
@login_required_
def user_about():
    return render_template('user_pages/user_detail.html')


@user.url_value_preprocessor
# @login_required_
def get_user(endpoint, values):
    u = User.query.filter_by(id=values.pop('user_id'))
    g.u = u.first_or_404()
