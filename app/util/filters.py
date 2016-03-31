# -*- coding:utf-8 -*-
"""
    
"""
from qblog import app

__author__ = 'Jux.Liu'


@app.template_filter()
def caps(text):
    return text.upper()
