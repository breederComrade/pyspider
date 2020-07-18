# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from flask import g

from app.core.db import db
from app.core.error import NotFound
from app.models.address import Address


class AddressDao():
    # 创建地址
    @staticmethod
    def create(form):
        with db.auto_commit():
            Address.create(
                commit=False,
                country=getattr(form, 'country', '中国'),
                province=getattr(form, 'province', None),
                city=getattr(form, 'city', None),
                detail=getattr(form, 'detail', None),
                name=getattr(form, 'name', None),
                mobile=getattr(form, 'mobile', None),
                customer_id=getattr(form, 'customer', None),
                geender=getattr(form, 'geender', True)
            )
    
    # 更新「配送信息」
    @staticmethod
    def update_address(id, user_id, **form):
        #
        # 查到地址修改
        address = Address.get_or_404(id=id)
        if not address.customer or address.customer.user_id != user_id:
            raise NotFound()
        address.update(**form)
    
    # 删除「配送信息」
    @staticmethod
    def delete_address(id, user_id):
        address = Address.get_or_404(id=id, user_id=user_id)
        address.delete()
