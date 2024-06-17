# -*- encoding = utf-8 -*-
from flask import request, jsonify, session

from app import app
from model import db, User


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'GET':
        return jsonify({"code": 400, "msg": "请求方法错误"})
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        
    user = db.session.query(User).filter(User.username == username).first()
    if user is None:
        return jsonify({"code": 400, "msg": "用户不存在，请注册"})
    if user.password != password:
        return jsonify({"code": 400, "msg": "密码错误，请重新输入"})
    if user.email != email:
        return jsonify({"code": 400, "msg": "邮箱错误，请重新输入"})

    if username == user.username and password == user.password and email == user.email:
        session['username'] = user.username
        session['is_login'] = True
        session.permanent = True
        return jsonify({"code": 200, "msg": "登录成功", "is_login": True})
    
# @app.route('/get_session', methods=['GET', 'POST'])
# def get_session():
#     # 要保持登录状态才能获取
#     print(session)
#     return jsonify({"code": 200, "session" : {"username": session.get('username'), "is_login": session.get('is_login')}})