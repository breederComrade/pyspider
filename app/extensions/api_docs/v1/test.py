# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/6/13
  author: wangjun
  description: 
  
"""

# 函数方法
from app.core.swagger_filed import BodyField

name = BodyField(name = 'name',type='string',description='名称')
id= BodyField(name='id',type='integer',description='id')

