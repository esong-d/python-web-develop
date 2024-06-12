# -*- encoding = utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, TIMESTAMP

from app import app
db = SQLAlchemy(app)


class User(db.Model):
    _tablename_ = 'user'
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    encrypt_md5 = db.Column(db.String(200), unique=False, nullable=False)
    email = db.Column(db.String(120))

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state"in dict:
            del dict["_sa_instance_state"]
        return dict

    def __repr__(self):
        return str({
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "encrypt_md5": self.encrypt_md5,
            "email": self.email
        })


class Article(db.Model):
    _tablename_ = 'article'
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return str({
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title
        })

class Product(db.Model):

    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    price = db.Column(db.Float)
    category = db.Column(db.String(100), unique=False, nullable=False)
    update_time = db.Column(TIMESTAMP, default=text('CURRENT_TIMESTAMP'))

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state"in dict:
            del dict["_sa_instance_state"]
        return dict
    
    def __repr__(self) -> str:
        return str({
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category
        })


with app.app_context():
    db.create_all()
