# coding: utf-8
from flask import render_template
from . import main

__author__ = 'Jux.Liu'


@main.route('/')
@main.route('/index')
def index():
    print
    return render_template('index.html')
