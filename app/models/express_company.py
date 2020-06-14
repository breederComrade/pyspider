# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db


class ExpressCompany(Base):
    __tablename__ = 'expressCompany'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(124),comment='快递公司名字')
    mobile = Column(Integer,comment='联系电话')
