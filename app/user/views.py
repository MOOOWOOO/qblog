# coding: utf-8
from .models import User
from . import user

__author__ = 'Jux.Liu'

@user.route('/<int:user_id>/', methods=['GET', 'POST'])
def user_main(user_id):
    return User.query.get(user_id)
