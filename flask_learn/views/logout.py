# -*- encoding = utf-8 -*-
from flask import session, jsonify

from app import app


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if not session:
        return jsonify({'code': 400, 'msg': '未登录'})
    session.pop("username")
    session.pop("is_login")
    session.clear()
    return jsonify({'code': 200, 'msg': '退出成功'})
