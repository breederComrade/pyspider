# 扩展
from flask import Flask as _Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()
# def init_marshmallow(app):
#     ma.init_app(app)
# 初始化app
def init_ext(app):
    # 初始化app
    db.init_app(app=app)
    ma.init_app(app=app)

    
