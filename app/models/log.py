# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/11.
  author: wangjun
  description:  操作和登录日志
  
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db


class Log(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(450), comment='日志信息')
    user_id = Column(Integer, nullable=False, comment='用户id')
    user_name = Column(String(20), comment='用户当时的昵称')
    status_code = Column(Integer, comment='http返回码')
    method = Column(String(20), comment='请求方法')
    path = Column(String(50),comment='请求路径')
    auth= Column(String(100), comment='访问权限')
    
    

