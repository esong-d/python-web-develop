# -*- encoding = utf-8 -*-

from app import app


@app.route('/', methods=['GET', 'POST'])
def logout():
    return 'welcome to logout'
    # url_for('home')
