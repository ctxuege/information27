from flask import session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from info import create_app,db
import logging

# manange.py 是启动程序的入口，只关心启动的相关参数及其内容，不关心如何创建app及相关业务逻辑

# 通过指定的配置名字创建对应配置的app
app = create_app('dev')

manager = Manager(app)
# 将app 与 db 关联
Migrate(app,db)
# 将迁移命令添加到manager
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()