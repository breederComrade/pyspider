# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/11.
  author: wangjun
  description:  关联表
  
"""
from sqlalchemy import Integer

from app.core.db import BaseModel as Base, db

# # 客户与用户关联
# customer_user = db.Table('customer_user',
#                          db.Column('customer_id', db.Integer, db.ForeignKey('customer.id')),
#                          db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
#                          )
# # 客户与企业关联
# customer_company = db.Table('customer_company',
#                             db.Column('customer_id', db.Integer, db.ForeignKey('customer.id')),
#                             db.Column('company_id', db.Integer, db.ForeignKey('company.id'))
#                             )


# 订单和商品
class OrderProduct(Base):
    __tablename__ = 'order_product'
    order_id = db.Column(Integer, primary_key=True, comment='联合外键,订单id')
    product_id = db.Column(Integer, primary_key=True, comment='联合外键,商品id')
    count = db.Column(Integer, nullable=False, comment='商品数量')
    def __init__(self, order_id=None, product_id=None, count=None):
        self.order_id = order_id
        self.product_id = product_id
        self.count = count
