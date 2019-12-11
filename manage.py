from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    """工程配置信息"""
    DEBUG = True

    # 为mysql 添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@47.98.142.158:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)

app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)


@app.route('/index')
def index():
    return 'index222'


if __name__ == '__main__':
    app.run(debug=True)