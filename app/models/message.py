# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/07/22.
  author: wangjun
  description: 消息
  
"""

from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger, Text, Float
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db

class Message(Base):
    id = Column(Integer,primary_key=True)
    content = Column(String(250),comment='消息')
    level= Column(Integer,comment='消息级别')
    

