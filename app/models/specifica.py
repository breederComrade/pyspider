# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/07/17.
  author: wangjun
  description: 规格
  
"""
from sqlalchemy import Column, Integer, String, ForeignKey, FLOAT
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base


class Specifica(Base):
    __tablename__ = 'spec'
    id = Column(Integer, primary_key=True)
    name = Column(String(45), comment='名称')
    price = Column(FLOAT, comment='价格')
    stock = Column(Integer, comment='库存')
    user_id = Column(Integer,comment='所属用户')
    
    # 一对多所属货品
    product_id = Column(Integer, ForeignKey('product.id'))
    # 一对多所属用户
    
    
    def __repr__(self):
        return '规格：{}'.format(self.name)
    
    def keys(self):
        return self.fields
