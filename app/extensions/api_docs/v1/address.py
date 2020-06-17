# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from app.core.swagger_filed import BodyField

name = BodyField(name='name', type='string', description='姓名', )
mobile = BodyField(name='mobile', type='string', description='手机号', )
email = BodyField(name='email', type='string', description='邮箱',)
province = BodyField(name='province', type='string', description='省',)
city = BodyField(name='city', type='string', description='市', )
country = BodyField(name='country', type='string', description='县区', )
detail = BodyField(name='detail', type='string', description='详细地址', )

