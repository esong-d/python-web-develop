# -*- encoding = utf-8 -*-

from flask import request, jsonify

from app import app
from model import User, db
from utils.password_encrypt import md5_encrypt

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        
        # 处理注册逻辑
        query = db.session.query(User).filter(User.username == name).first()
        if query:
            return jsonify({"code": 400, 'message': '用户名已存在, 请重新注册'})
        
        user = User(username=name, password=password, encrypt_md5=md5_encrypt(password),email=email)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"code": 500, 'message': '注册失败'})
        
        # 返回注册结果
        return jsonify({"code": 200, 'message': '注册成功'})