# _*_ coding: utf-8 _*_
"""
  Created by wangjun on 2020/06/10.
  __author__ = 'wangjun'
"""

# 客户表

from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(24), comment='名称')
    avatar = Column(String(123), comment='头像')
    mobile = Column(String(24), comment='手机号')
    wechat = Column(String(124), comment='微信号')

    # 状态
    status = Column(Boolean,default=False, nullable=False, comment='是否启用')
    # 一对多
    user_id = Column(Integer, ForeignKey('user.id'), comment='所属用户')
    # 关联地址 一对多
    address = relationship('Address', backref=backref('customer'))
    # 微信号
    # 关联用户 多对多
    # user = relationship('User', secondary='customer_user',backref = backref('customer',lazy='dynamic'))
#  所属企业
#  company = relationship('Company',secondary = 'customer_company',backref= backref('customer',lazy='dynamic'))
    def keys(self):
        return self.fields
        
