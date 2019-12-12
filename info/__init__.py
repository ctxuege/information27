from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
# 可以指定session存储的位置
from flask_session import Session

from config import config


app = Flask(__name__)

app.config.from_object(config["dev"])

# 初始化数据库
db = SQLAlchemy(app)

# 初始化redis 存储对象
redis_store = StrictRedis(host=config["dev"].REDIS_HOST,port=config["dev"].REDIS_HOST,password=config["dev"].REDIS_PASSWORD)
# 开启当前项目 CSRF 保护, 只做服务器验证功能
CSRFProtect(app)
# 设置session保存指定位置
Session(app)