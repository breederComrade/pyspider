# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/07/22.
  author: wangjun
  description: 规格
  
"""
from flask import g

from app.core.db import db
from app.core.error import NotFound
from app.models.product import Product
from app.models.specifica import Specifica


class SpecDao():
    
    @staticmethod
    def create(form):
        '''创建'''
        with db.auto_commit():
            # 判断指定货品是否存在
            product = Product.query.filter_by(id = form.product_id,user_id=g.user.id).first_or_404(msg='指定商品id不存在')
            Specifica.create(
                commit=False,
                name=getattr(form, 'name', None),
                price=getattr(form, 'price', None),
                stock=getattr(form, 'stock', None),
                product_id=getattr(form, 'product_id', None),
                user_id = g.user.id
            )
    
    @staticmethod
    def update(id,**form):
        '''修改'''
        # 验证是否存在id
        spec = Specifica.query.filter_by(id = id,user_id=g.user.id).first_or_404()
        spec.update(**form)
        
        pass
    
    @staticmethod
    def delete(id):
        '''删除'''
        spec = Specifica.query.filter_by(id = id,user_id=g.user.id).first_or_404()
        spec.delete()
    
    @staticmethod
    def get(id):
        '''详情'''
        spec = Specifica.query.filter_by(id = id,user_id=g.user.id).first_or_404()
        # 判断是否是当前用的所属于
        return spec
    
    @staticmethod
    def list(productId,page,size):
        '''列表'''
        paginator = Specifica.query.filter_by(product_id=productId,user_id=g.user.id).paginate(page=page, per_page=size, error_out=False)
        return {
            'total': paginator.total,
            'current_page': paginator.page,
            'items': paginator.items
        }

