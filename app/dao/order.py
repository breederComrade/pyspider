# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/07/20.
  author: wangjun
  description: 订单DAO
  
"""
from flask import g
from sqlalchemy import desc

from app.core.db import db
from app.core.error import Success
from app.models.m2m import Order2Product
from app.models.order import Order


class OrderDao(object):
    
    @staticmethod
    def create(form):
        '''创建'''
        with db.auto_commit():
            order = Order()
            order.user_id = 41
            order.discount = getattr(form,'discount',None)
            order.remark = getattr(form,'remark',None)
            order.order_status = getattr(form,'status_id',None)
            order.total_count = getattr(form,'totalcount',None)
            order.total_price = getattr(form,'totalprice',None)
            db.session.add(order)
            db.session.flush()  # 刷新数据库缓存，不操作事务
            order_id = order.id  # 获取更新后的order信息
            products = getattr(form,'products',None)
            db.session.add_all(
                [
                    Order2Product(order_id, p['id'], p['num'],p['price']) for p in products
                ]
            )
            
        # 创建订单
        # 创建订单货品
        
        
    
    @staticmethod
    def update():
        '''修改'''
        pass
    
    @staticmethod
    def get():
        '''获取详情'''
        pass
    
    @staticmethod
    def list():
        '''获取列表'''
        pass
