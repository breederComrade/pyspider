# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/07/22.
  author: wangjun
  description: 
  
"""

from app.core.swagger_filed import BodyField, IntegerQueryFiled
name = BodyField(name='name', description='规格名', type='string',default='xx')
price = BodyField(name='price',description='单价',type='integer')
stock = BodyField(name='stock' , description='库存',type='integer')
product_id = BodyField(name='product_id', description='货品id',type='integer')