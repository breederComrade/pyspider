# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/07/22.
  author: wangjun
  description: 提醒信息
  
"""

from app.extensions.api_docs.redprint import Redprint


api = Redprint(name='message', description='信息', )

@api.route('',methods = ['POST'])
@api.doc()
def send():
    '''发送消息'''
    return 'ffff'

