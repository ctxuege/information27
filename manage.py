from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect


class Config(object):
    """工程配置信息"""
    DEBUG = True

    # 为mysql 添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@47.98.142.158:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis 配置
    REDIS_HOST = "115.238.87.197"
    REDIS_PORT = 6380


app = Flask(__name__)

app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis 存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_HOST)
# 开启当前项目 CSRF 保护, 只做服务器验证功能
CSRFProtect(app)


@app.route('/')
def index():
    return 'index222'


if __name__ == '__main__':
    app.run(debug=True)