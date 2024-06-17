# -*- encoding = utf-8 -*-
from flask import Blueprint, request, jsonify
import json

from app import app
from utils.redis import redis
from utils.datetime2str import datetime_format
from model import Product, db


product_bp = Blueprint('product', __name__)


@product_bp.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'GET':
        name = request.args.get('name')
        price = request.args.get('price')
        category = request.args.get('category')
        
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category = request.form.get('category')
    
    print("value: ", name, price, category)
    try:
        db.session.add(Product(name=name, price=price, category=category))
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({"code": 500, "msg": "add filed", "data": "新增用户商品失败！"})
    return jsonify({"code": 200, "msg": "add success", "data": "新增用户商品成功！"})



@product_bp.route('/query', methods=['POST', 'GET'])
def query():
    if request.method == 'GET':
        pageNum = request.args.get('pageNum')
        pageSize = request.args.get('pageSize')
    if request.method == 'POST':
        pageNum = request.get_json().get('pageNum')
        pageSize = request.get_json().get('pageSize')
    if not pageNum or not pageSize:
        return jsonify({"code": 500, "data": "null", "msg": "参数错误，查询失败"})
    if redis.get(key=str(pageNum)):
        return jsonify({"code": 500, "data": json.loads(redis.get(str(pageNum))), "msg": "查询成功"})
    try:
        data = db.session.query(Product).order_by(Product.id).paginate(page=int(pageNum), per_page=int(pageSize))
        data = datetime_format([i.to_json() for i in data.items])
        # 存储到redis
        redis.set(key=str(pageNum), value=json.dumps(data))
        return jsonify({"code": 200, "data": data, "msg": "查询成功"})
    except Exception as e:
        print(e)
        return jsonify({"code": 500, "data": "null", "msg": "查询失败"})


app.register_blueprint(product_bp, url_prefix='/product')