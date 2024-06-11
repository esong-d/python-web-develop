# -*- encoding = utf-8 -*-

from app import app


@app.route('/login', methods=['POST'])
def login():
    return "welcome to login page"