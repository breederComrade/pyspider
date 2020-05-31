# 模型
from datetime import datetime

from app.extension import db


class BaseModel(db.Model):
    __abstract__ = True
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class GoodsModel(BaseModel):
    __tablename = 'goods_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), unique=True, )
    no = db.Column(db.String(45), unique=True)
    num = db.Column(db.Integer, default=12, nullable=True)
    
    def __repr__(self):
        return '<货品 %r>' % self.name

# 订单表
class OrderModel(BaseModel):
    __tablename__ = 'order_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

# 订单货品详情
class OrderGoodsModel(BaseModel):
    __tablename__ = 'order_goods_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)



# 客户表
class CustomerModel(BaseModel):
    __tablename__ = 'customer_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


# 地址表
class AddressModel(BaseModel):
    __tablename__ = 'address_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


# 用户表
class UseModel(BaseModel):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)




# 物流公司表
class ExpressModel(BaseModel):
    __tablename__= 'express_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)