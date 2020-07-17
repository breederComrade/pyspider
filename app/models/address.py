# _*_ coding: utf-8 _*_
"""
  Created by wangjun on 2020/06/10.
  __author__ = 'wangjun'
  
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.core.db import EntityModel as Base

"""
 地址跟随客户信息 客户可有多个地址
"""


class Address(Base):
 
    '''配送信息'''
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, autoincrement=True)
    default = Column(Boolean,default=False,comment='是否默认地址')
    name = Column(String(30), nullable=False, comment='收货人姓名')
    mobile = Column(String(20), nullable=False, comment='手机')
    province = Column(String(20), comment='省份')
    city = Column(String(20), comment='城市')
    country = Column(String(20), comment='县区')
    detail = Column(String(100), comment='详细地址')
    geender = Column(Boolean,comment='性别')
    
    # 客户列表
    customer_id = Column(Integer,ForeignKey('customer.id'), comment='外键:关联客户id')
    
    def keys(self):
        self.hide('id', 'user_id')
        return self.fields
