# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/30.
  author: wangjun
  description: 权限
  
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Float, SmallInteger
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db


class Permission(Base):
    '''权限'''
    __tablename__ = 'permission'
    id = Column(Integer, primary_key=True,autoincrement=True )
    name = Column(String(45),comment='权限名称')
    desc = Column(String(45),comment = '操作权限名称')
    parent_id = Column(Integer,comment='父权限id')
    
    
    
