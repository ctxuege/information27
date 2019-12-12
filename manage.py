from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
# 可以指定session存储的位置
from flask_session import Session
from flask_script import Manager

class Config(object):
    """工程配置信息"""
    DEBUG = True

    SECRET_KEY = "FiSZ+xxGvsGdVTJVMRtY8vp8OwYtD2pvHE6AyvI9kWnG+soU4zY00GS2zP4jH2oW"

    # 为mysql 添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@47.98.142.158:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis 配置
    REDIS_HOST = "115.238.87.197"
    REDIS_PORT = 6381
    REDIS_PASSWORD = 'yq2018'

    # session配置
    SESSION_TYPE = "redis"
    # 是否开启session签名
    SESSION_USE_SIGNER = True
    # 指定session 保存到redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD)
    # 设置session 过期
    SESSION_PERMANENT = False
    # 设置过期时间
    permanent_session_lifetime = 86400 * 2


app = Flask(__name__)

app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis 存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_HOST,password=Config.REDIS_PASSWORD)
# 开启当前项目 CSRF 保护, 只做服务器验证功能
CSRFProtect(app)
# 设置session保存指定位置
Session(app)


manager = Manager(app)


@app.route('/')
def index():
    session["name"] = "itheima"
    return 'index222'


if __name__ == '__main__':
    manager.run()