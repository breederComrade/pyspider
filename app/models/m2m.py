# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/11.
  author: wangjun
  description:  关联表
  
"""
from app.core.db import db

# 客户与用户关联
customer_user= db.Table('customer_user',
                db.Column('customer_id', db.Integer, db.ForeignKey('customer.id')),
                db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
                )
# 客户与企业关联
customer_company= db.Table('customer_company',
                db.Column('customer_id', db.Integer, db.ForeignKey('customer.id')),
                db.Column('company_id', db.Integer, db.ForeignKey('company.id'))
                )
