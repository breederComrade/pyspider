# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/07/17.
  author: wangjun
  description: 客户
  
"""
from app.core import db
from app.models.customer import Customer


class CustomerDao(object):
    @staticmethod
    def create(form):
        '''创建'''
        with db.auto_commit():
            # 判断重复
            if hasattr(form, 'name'):
                Customer.abort_repeat(name=form.name, msg='该客户已被使用！')
            # 判断是否存在
            Customer.create(
                commit=False,
                name=getattr(form, 'name', None),
                mobile =getattr(form, 'mobile', None),
                wechat =getattr(form, 'wechat', None),
                avatar =getattr(form, 'avatar', None),
                status = getattr(form,'status',True)
            )
    
    @staticmethod
    def update(id,form):
        '''修改'''
        
    @staticmethod
    def get(id):
        '''详情'''
        pass
    
    @staticmethod
    def list(form):
        '''查询列表'''
        pass
    

