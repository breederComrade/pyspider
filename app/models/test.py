# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/18.
  author: wangjun
  description: 
  
"""
from sqlalchemy import Column, Integer, String

from app.core.db import EntityModel as Base


class Test(Base):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(45), comment='名称')

    
    def __repr__(self):
        return 'Text:{}'.format(self.name)
    
    def keys(self):
        return self.fields
