# coding: utf-8
from flask import render_template
from . import user
from .models import User

__author__ = 'Jux.Liu'


@user.route('/<int:user_id>/', methods=['GET', 'POST'])
def user_main(user_id):
    u = User.query.get(user_id)
    return render_template('user_pages/user_detail.html', user=u)
