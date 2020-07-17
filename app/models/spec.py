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


class Spec(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, comment='名称')
    size = Column(FLOAT,comment='尺寸')
    weight = Column(FLOAT,comment='重量')
    def __repr__(self):
        return '规格：{}'.format(self.name)
    
    def keys(self):
        return self.fields;
