# _*_ coding: utf-8 _*_
"""
  Created by wangjun on 2020/06/10.
  __author__ = 'wangjun'
    description: 用户组

  
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True, comment='权限组名称')
    info = Column(String(255), comment='权限组描述')
    user = relationship('Uer', second='user_group', backref=backref('user', lazy='dynamic'))
