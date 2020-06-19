# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/19.
  author: wangjun
  description: 授权权限
  
"""
from app.core.error import Success
from app.extensions.api_docs.redprint import Redprint
from app.models.auth import Auth

api = Redprint(name='auth', description='权限')


@api.route('/list', methods=['GET'])
@api.doc()
def list():
    '''获取所有可分配权限'''
    auth = Auth.get_or_404(id=1)
    return Success()


@api.route('/by_group', methods=['GET'])
@api.doc()
def list_group():
    '''查看权限组所有权限'''
    auth = Auth.get_or_404(id=1)
    return Success()


@api.route('/by_group', methods=['DELETE'])
@api.doc()
def del_in_group():
    '''删除权限组下所有权限'''
    auth = Auth.get_or_404(id=1)
    return Success()


@api.route('/remove', methods=['DELETE'])
@api.doc()
def remove():
    '''删除多个可分配权限'''
    auth = Auth.get_or_404(id=1)
    return Success()


@api.route('/append', methods=['PUT'])
@api.doc()
def append():
    '''新增多个可分配权限'''
    auth = Auth.get_or_404(id=1)
    return Success()
