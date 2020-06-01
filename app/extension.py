# 扩展
from flask import Flask as _Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# 初始化app
def init_ext(app):
    # 初始化app
    db.init_app(app=app)

