# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/07/17.
  author: wangjun
  description: 规格
  
"""

from app.core.error import Success
from app.extensions.api_docs.redprint import Redprint
from app.core.token_auth import auth
from app.models.role import Role

api = Redprint(name='spec', description='规格')


@api.route('', methods=['GET'])
@api.doc()
def get():
    '''获取规格'''
    return Success()


@api.route('', methods=['POST'])
@api.doc()
def create():
    '''新增规格'''
    return Success()


@api.route('', methods=['DELETE'])
@api.doc()
def delete():
    '''删除规格'''
    return Success()


@api.route('', methods=['PUT'])
@api.doc()
def update():
    '''修改规格'''
    return Success()


@api.route('/list', methods=['GET'])
@api.doc()
def list():
    '''获取规格列表'''
    return Success()
