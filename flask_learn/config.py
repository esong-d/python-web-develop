# -*- encoding = utf-8 -*-

from datetime import timedelta

DEBUG = True

# session config
SECRET_KEY = "1234567890"
PERMANENT_SESSION_LIFETIME = timedelta(days=7)

# redis config
REDIS_URL = "redis://127.0.0.1:6379/0"

# mysql config
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:abc123456@127.0.0.1:3306/flask_project?charset=utf8mb4"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
SQLALCHEMY_ENCODING = "utf8mb4"
