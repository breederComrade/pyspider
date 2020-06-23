# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/16.
  author: wangjun
  description: 权限组
  
"""
from app.core.token_auth import auth
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import group as api_doc

api = Redprint(name='group', description='权限组管理', alias='group',api_doc=api_doc)


@api.route('', methods=['POST'])
@api.doc(args=['name','info'])
@auth.admin_required
def create():
    '''新建权限组'''
    return '新增权限'


@api.route('', methods=['GET'])
@api.doc(args=['g.query.group_id'])
def get():
    '''获取中权限组权限'''
    return '获取中权限组权限'


@api.route('', methods=['PUT'])
@api.doc(args=['g.query.group_id','name','info'])
def update():
    '''更新权限组'''
    return '更新权限组'


@api.route('', methods=['DELETE'])
@api.doc(args=['g.body.group_id'])
def delete():
    '''删除权限组'''
    return '删除权限组'


@api.route('/list', methods=['GET'])
@api.doc()
def list():
    '''权限组列表'''
    return '权限列表'
