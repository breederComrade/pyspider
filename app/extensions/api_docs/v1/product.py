# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/17.
  author: wangjun
  description: 商品
  
"""
from app.core.swagger_filed import BodyField
# 分类id
category_id = BodyField(name='category_id',type='integer',description='分类id',default=0,enum=[0])
# 商品id
product_id = BodyField(name='id', type='integer', description='商品id',default=1,enum=[1])
#
name = BodyField(name='name', type='string', description='商品名称',default='棒棒',enum=["棒棒'"])
price = BodyField(name='price', type='integer', description='价格',default=123,enum=[123])
stocknum = BodyField(name='stocknum', type='integer', description='库存量',default=22323,enum=[123,22323])
remark = BodyField(name='remark', type='string', description='备注')

imgs = BodyField(name='images', type='array', description='图片', default={
    "file_path": '',
    "file_url": '',
    "file_name": ''
},enum=[{
    "file_path": '',
    "file_url": '',
    "file_name": ''
},{
    "file_path": '',
    "file_url": '',
    "file_name": ''
}])

# 分类id
