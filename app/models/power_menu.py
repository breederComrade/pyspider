# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/6/28
  author: wangjun
  description: 菜单权限表
  
"""

from sqlalchemy import Column, Integer, String

from app.core.db import EntityModel as Base


class PowerMenu(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(20), comment='权限名称')
    description = Column(String(45), comment='描述')
    
    def __repr__(self):
        return '名称:{}' .format(self.name)
    
    def keys(self):
        return self.fields
