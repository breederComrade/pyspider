# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/16.
  author: wangjun
  description: 权限组
  
"""
from app.extensions.api_docs.redprint import Redprint

api = Redprint(name='group', description='权限组管理', alias='group')


@api.route('', methods=['POST'])
@api.doc()
def create():
    '''新建权限组'''
    return '新增权限'


@api.route('', methods=['GET'])
@api.doc()
def get():
    '''获取中权限组权限'''
    return '获取中权限组权限'


@api.route('', methods=['PUT'])
@api.doc()
def update():
    '''更新权限组'''
    return '更新权限组'


@api.route('', methods=['DELETE'])
@api.doc()
def delete():
    '''删除权限组'''
    return '删除权限组'


@api.route('/list', methods=['GET'])
@api.doc()
def list():
    '''权限组列表'''
    return '权限列表'
