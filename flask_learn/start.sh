# 创建虚拟环境
virtualenv -p python3 .env

# 激活虚拟环境
source .env/bin/activate

# 安装Flask依赖
pip3 install -r requirements.txt


# 启动Flask应用, 本地运行，不使用uwsgi
# python3 app.py
# 注意：如果需要使用uwsgi，请使用uwsgi命令启动,并且配置nginx
# 启动：uwsgi --ini uwsgi.ini
# 重启：uwsgi --reload uwsgi.pid
# 停止：uwsgi --stop uwsgi.pid
