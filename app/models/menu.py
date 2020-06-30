# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/30.
  author: wangjun
  description: 表单操作权限
  
"""

from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger, Text, Float
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db


class Menu(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, comment='菜单名字')
    url = Column(String, comment='菜单地址')
    parent_id = Column(Integer,comment='父级id')
