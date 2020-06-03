# 扩展
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
ma = Marshmallow()
# 初始化app
def init_ext(app):
    # 初始化app
    db.init_app(app)
    ma.init_app(app)
