# -*- encoding = utf-8 -*-
from app import app
from flask import request, jsonify, Blueprint

from utils.password_encrypt import md5_encrypt
from model import db, User


base_bp = Blueprint("user", __name__)


@base_bp.route('/new', methods=['POST', 'GET'])
def new_user():
    if request.method == 'POST':
        name = request.form.get('name')
        pwd = request.form.get('password')
        email = request.form.get('email')
        print(name, pwd, email)
        query = db.session.query(User).filter(User.username == name).first()
        # print("查询结果", query)
        if query:
            return jsonify({'code': 400, 'msg': '请求失败', 'data': "用户名已存在", 'text': '用户名已存在'})
        print(name, pwd, email)
        try:
            db.session.add(User(username=name, password=pwd, email=email, encrypt_md5=md5_encrypt(pwd)))
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
            return jsonify({'code': 400, 'msg': '请求失败', 'data': e, 'text': '创建用户失败'})
        return jsonify({'code': 200, 'msg': '请求成功', 'data': {"name": name, "pwd": md5_encrypt(pwd), "email": email}, 'text': '创建用户成功'})
    if request.method == 'GET':
        return jsonify({'code': 200, 'msg': '请求成功', 'text': '请输入用户名和密码'})


@base_bp.route('/query', methods=['POST', 'GET'])
def query():
    if request.method == 'POST':
        page = int(request.get_json().get('pageNum'))
        pages_size = int(request.get_json().get('pageSize'))
        query = db.session.query(User)
        if query.count() > 0:
            data = query.order_by(User.username.desc()).paginate(page=page, per_page=pages_size)
            data = [i.to_json() for i in data.items]
            return jsonify({'code': 200, 'msg': '请求成功', 'data': data, 'text': 'success'})
        return jsonify({'code': 400, 'msg': '请求失败', 'data': 'null', 'text': '没有数据'})
    if request.method == 'GET':
        page = int(request.args.get('page'))
        page_size = int(request.args.get('page_size'))
        query = db.session.query(User)
        if query.count() > 0:
            data = query.order_by(User.username.desc()).paginate(page=page, per_page=page_size)
            data = [i.to_json() for i in data.items]
            print(data)
            return jsonify({'code': 200, 'msg': '请求成功', 'data': data, 'text': 'success'})
        return jsonify({'code': 400, 'msg': '请求失败', 'data': 'null', 'text': '没有数据'})


@base_bp.route('/change_user', methods=['POST'])
def change_user():
    name = request.form.get('name')
    old_pwd = request.form.get('old_pwd')
    new_pwd = request.form.get('new_pwd')
    email = request.form.get('email')
    print(name, old_pwd, new_pwd, email)
    if old_pwd == db.session.query(User).filter(User.username == name).first().password \
            and email == db.session.query(User).filter(User.username == name).first().email:
        db.session.query(User).filter(User.username == name).update({'password': new_pwd})
        db.session.commit()
    else:
        return {"msg": "输入数据错误", "code": "404"}
    return jsonify({"msg": "change_user success", "code": 200})


@base_bp.route('/delete', methods=['GET'])
def delete_user():
    name = request.args.get('name')
    if not name:
        return jsonify({"msg": "delete_user error", "code": "404", "text": "请输入用户名"})

    count = db.session.query(User).filter(User.username == name).count()
    if count == 0:
        return jsonify({"msg": "delete_user error", "code": "404", "text": "用户不存在"})

    try:
        db.session.query(User).filter(User.username == name).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({"msg": "delete_user error", "code": "404", "text": str(e)})

    return jsonify({"msg": "delete_user success", "code": 201, "text": name + " 删除成功"})


app.register_blueprint(base_bp, url_prefix="/user")
