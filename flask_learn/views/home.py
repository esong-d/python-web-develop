# -*- encoding = utf-8 -*-

from app import app
from flask import Blueprint

home_bp = Blueprint('home', __name__)


@home_bp.route('/', methods=['GET', 'POST'])
def home():
    return "hello world"


app.register_blueprint(home_bp, url_prefix='/home')
