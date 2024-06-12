# -*- encoding = utf-8 -*-

from app import app
from flask import Blueprint


@app.route('/')
@app.route('/home')
def home():
    return "home page"



