# _*_ coding: utf-8 _*_
"""
  Created by wangjun on 2020/06/10.
  __author__ = 'wangjun'
"""
from sqlalchemy import Column, Integer, String

from app.core.db import EntityModel as Base
class Auth(Base):
    __tablename__ = 'auth'
    id = Column(Integer,primary_key=True,autoincrement=True)
    group_id = Column(Integer,nullable=False,comment='所属权限组')
    name = Column(String(60),comment='权限字段')
    module = Column(String(50),comment='权限的模块')
    