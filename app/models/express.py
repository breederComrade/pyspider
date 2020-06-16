# _*_ coding: utf-8 _*_
"""
  Created by wangjun on 2020/06/10.
  __author__ = 'wangjun'
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db


class Express(Base):
    __tablename__ = 'express'
    id = Column(Integer, primary_key=True, autoincrement=True)
    info =Column(String(124),comment='物流信息')
    # 关联订单 一对一
    order_id = Column(Integer,ForeignKey('order.id'))
#

    

    
