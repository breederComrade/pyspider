# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/6/11
  author: wangjun
  description: 用于自定义用户列表
  
"""

# 字段

from app.core.swagger_filed import BodyField

email = BodyField(name='email', type='string', description='邮箱', enum=['1871015627@qq.com'])
nickname = BodyField(name='nickname', type='string', description='昵称', enum=['admin','superadmin','user'])
account = BodyField(name='account', type='string', description='', enum=["666@qq.com"])
password = BodyField(name='password', type='string', description='密码', enum=['123456'])
type = BodyField(name='type', type='integer', description='登录方式', enum=[101])


