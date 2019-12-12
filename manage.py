from flask import session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from info import create_app,db
import logging


# 通过指定的配置名字创建对应配置的app
app = create_app('dev')

manager = Manager(app)
# 将app 与 db 关联
Migrate(app,db)
# 将迁移命令添加到manager
manager.add_command('db',MigrateCommand)


@app.route('/')
def index():
    # session["name"] = "itheima"
    # 测试打印日志
    logging.info('start turn in.......')
    return 'index'


if __name__ == '__main__':
    manager.run()