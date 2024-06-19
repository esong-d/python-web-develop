# -*- encoding = utf-8 -*-
from flask import Flask
from flask_cors import CORS
from gevent import pywsgi

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')

from views.home import *
from views.register import *
from views.login import *
from views.logout import *
from views.product import *
from views.user import *
from model import *


if __name__ == '__main__':
    # 开发环境启动程序(单线程)
    # app.run(host='127.0.0.1', port=9090)
    # 生产环境启动程序(多线程)
    server = pywsgi.WSGIServer(('127.0.0.1', 9090), app)
    server.serve_forever()
