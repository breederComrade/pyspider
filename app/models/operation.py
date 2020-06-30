# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/30.
  author: wangjun
  description: 操作权限
  
"""

from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger, Text, Float
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db


class Operation(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    able_edit = Column(Integer, comment='允许编辑')
    able_delete = Column(Integer, comment='允许删除')
    albe_find = Column(Integer, comment='允许查询')
