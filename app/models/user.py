# _*_ coding: utf-8 _*_
"""
  Created by wangjun on 2020/06/10.
  author:wangjun
  project:有单生意
  description: 用户模型
  
"""
from flask import g, request, current_app
from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), comment='昵称')
    account = Column(String(45), comment='账号')
    group_id = Column(Integer, comment='用户所属的权限组id',
                      default=0)
    # 一对多 客户信息
    customer = relationship('Customer', backref=backref('user'))
    # 订单
    order = relationship('Order', backref=backref('user'))
    # 所属公司
    commpany_id = Column(Integer, ForeignKey('commany.id'), nullable=False, comment='外键公司id')  # 下单用户ID
    
    def __repr__(self):
        return 'id:{} ====  账号:{}====昵称:{}'.format(self.id,self.account,self.nickname)
    
    # 序列化返回数据
    def keys(self):
        return self.fields
    
    # 用户名
    @property
    def userName(self):
        return self.userName
    
    # 用户手机号
    @property
    def moblie(self):
        return
    
    # email
    @property
    def email(self):
        return
    
    # avatar
    @property
    def avatar(self):
        return ''
    
    
    # 是否是超级管理员
    @property
    def is_admin(self):
        #
        return True

    # 当前用户
    @classmethod
    def get_current_user(cls):
        '''获取当前用户'''
        return g.user
    
    
    
    