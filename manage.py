from flask import Flask, redirect

from werkzeug.middleware.proxy_fix import ProxyFix


from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import create_app
# 创建
app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)
manager = Manager(app=app)

'''
实际操作顺序:
1.python 文件 db init
2.python 文件 db migrate -m"版本名(注释)"
3.python 文件 db upgrade 然后观察表结构
4.根据需求修改模型
5.python 文件 db migrate -m"新版本名(注释)"
6.python 文件 db upgrade 然后观察表结构
7.若返回版本,则利用 python 文件 db history查看版本号
8.python 文件 db downgrade(upgrade) 版本号
'''

#
# Migrate(app,db)

# 添加命令
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
