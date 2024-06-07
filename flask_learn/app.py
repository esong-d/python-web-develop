# -*- encoding = utf-8 -*-
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

from view import *
from model import *

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9090)
