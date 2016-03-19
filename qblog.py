# coding: utf-8
from app import create_app

__author__ = 'Jux.Liu'

app = create_app()

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
