# coding: utf-8
from flask import Blueprint

__author__ = 'Jux.Liu'
bp=Blueprint('blog', __name__)

@bp.route('/')
def index():
    return "hello world!"