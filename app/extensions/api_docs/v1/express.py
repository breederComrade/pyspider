# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/17.
  author: wangjun
  description: 物流信息
  
"""
from app.core.swagger_filed import BodyField

datetime = BodyField(
    name='datetime',type='string',description='时间'
)
data = BodyField(
    name='data',type = 'string',description='内容'
)
status_id = BodyField(
    name='data',type='integer',description='状态id'
)
status = BodyField(
    name='data',type='string',description='状态'
)

