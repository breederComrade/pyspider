# 模型
from datetime import datetime

from app.extension import db


class BaseModel(object):
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class GoodsModel(BaseModel, db.Model):
    __tablename = 'goods_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), unique=True, )
    no = db.Column(db.String(45), unique=True)
    num = db.Column(db.Integer, default=12, nullable=True)
    
    def __repr__(self):
        return '<货品 %r>' % self.name
