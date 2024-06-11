# -*- encoding = utf-8 -*-
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

from views.home import *
from views.login import *
from views.logout import *
from views.product import *
from views.user import *
from model import *


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9090)
