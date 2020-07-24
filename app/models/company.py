# _*_ coding: utf-8 _*_
"""
  Created by wangjun on 2020/06/10.
  description:
"""

# 企业表

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), comment='昵称')
    avatar = Column(String(123), comment='头像')
    mobile = Column(String(24), comment='手机号')
    
