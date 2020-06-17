# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/17.
  author: wangjun
  description: 商品
  
"""
from app.core.swagger_filed import BodyField

product_id = BodyField(name='id', type='integer', description='商品id')
name = BodyField(name='name', type='string', description='商品名称')
price = BodyField(name='price', type='integer', description='价格')
stocknum = BodyField(name='stocknum', type='integer', description='库存量')
remark = BodyField(name='remark', type='string', description='备注')
imgs = BodyField(name='images',type='array',description='图片')