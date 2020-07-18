# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from app.core.swagger_filed import BodyField, IntegerQueryFiled

name = BodyField(name='name', type='string', description='姓名', )
mobile = BodyField(name='mobile', type='string', description='手机号', )
email = BodyField(name='email', type='string', description='邮箱',)
province = BodyField(name='province', type='string', description='省',)
city = BodyField(name='city', type='string', description='市', )
country = BodyField(name='country', type='string', description='国家',default='中国' )
detail = BodyField(name='detail', type='string', description='详细地址', )
customer = BodyField(name='customer',type='integer',description='关联客户id')
# 客户id
customer_in_query = IntegerQueryFiled(name='id', description='客户id', default=0)

