# _*_ coding: utf-8 _*_
"""
  Created by wangjun on 2020/06/10.
  __author__ = 'wangjun'
"""

from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger, Text, Float
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db
class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer,primary_key=True,autoincrement=True)
    order_no = Column(String(20), unique=True,comment='订单号')
    user_id = Column(Integer,ForeignKey('user.id'), nullable=False, comment = "外键 下单用户id" )
    # 商品id
    products = relationship('OrderProduct',backref = 'order')
    
    #
    order_status = Column(SmallInteger,default=1,comment='订单状态')
    remark = Column(Text,comment='订单备注')
    total_count = Column(Integer,comment='订单货总个数')
    total_price = Column(Float, comment='订单总价')
    prepay_id = Column(String(100), unique=True, comment='预付款id')
    
    def keys(self):
        return self.fields
    
    
    
    
    