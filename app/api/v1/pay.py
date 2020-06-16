# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""

from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import user as api_doc

api = Redprint(name='pay', description='支付', )


@api.route('', methods=['GET'])
@api.doc()
def get_pay():
    '''单笔支付记录'''
    return 'pay'


@api.route('/<int:userId>', methods=['GET'])
@api.doc()
def getByUserId(userId):
    '''指定用户支付记录'''
    return '指定用户支付记录'


# 创建支付记录
@api.route('', methods=['PUT'])
@api.doc()
def create():
    '''创建支付几率'''
    return '创建支付记录'


@api.route('', methods=['DELETE'])
@api.doc()
def delete():
    '''删除支付记录'''
    return 'pay'


@api.route('/list', methods=['POST'])
@api.doc()
def list():
    '''所有用户的支付记录'''
    return 'pay'
