from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
# 可以指定session存储的位置
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from config import Config


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
# 将app 与 db 关联
Migrate(app,db)
# 将迁移命令添加到manager
manager.add_command('db',MigrateCommand)


@app.route('/')
def index():
    session["name"] = "itheima"
    return 'index'


if __name__ == '__main__':
    manager.run()