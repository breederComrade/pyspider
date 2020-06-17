# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/17.
  author: wangjun
  description: 
  
"""
from app.core.swagger_filed import BodyField

name = BodyField(name='name',type='string',description='权限名称')
info= BodyField(name='info',type='string',description='信息')

