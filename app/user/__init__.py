# coding: utf-8
from flask import Blueprint

__author__ = 'Jux.Liu'

user = Blueprint('user', __name__, url_prefix='user')

from . import views
