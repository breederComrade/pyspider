# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/11.
  author: wangjun
  description:  关联表
  
"""
from sqlalchemy import Integer, Column, ForeignKey

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


# 用户企业关联
user_company = db.Table(
    'user_company',
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True, comment='用户外键'),
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True, comment='企业外键'),
)

# 用户组表
user_group = db.Table(
    'user_group',
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True, comment='用户外键'),
    Column('group_id', Integer, ForeignKey('group.id'), primary_key=True, comment='组外键')
)

# 用户角色表
user_role = db.Table(
    'user_role',
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True, comment='用户外键'),
    Column('role_id', Integer, ForeignKey('role.id'), primary_key=True, comment='角色外键')
)

# 组权限表
group_permission = db.Table(
    'group_permission',
    Column('group_id', Integer, ForeignKey('group.id'), primary_key=True, comment='组外键'),
    Column('permission_id', Integer, ForeignKey('permission.id'), primary_key=True, comment='权限外键')
)
# 角色权限表
role_permission = db.Table(
    'role_permission',
    Column('role_id', Integer, ForeignKey('role.id'), primary_key=True, comment='角色外键'),
    Column('permission_id', Integer, ForeignKey('permission.id'), primary_key=True, comment='权限外键')
)


# 用户权限表
user_permission = db.Table(
    'user_permission',
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True, comment='角色外键'),
    Column('permission_id', Integer, ForeignKey('permission.id'), primary_key=True, comment='权限外键')
)