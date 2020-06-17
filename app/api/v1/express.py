# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/16.
  author: wangjun
  description: 物流信息
  
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import express as api_doc

api = Redprint(name='express', description='物流信息', api_doc=api_doc)


@api.route('', methods=['GET'])
@api.doc(args=['g.query.id'])
def get():
    '''单个物流信息'''
    return '单个物流信息'


@api.route('', methods=['POST'])
@api.doc(args=['datetime','status_id','data'])
def create():
    '''新增物流信息'''
    return '新增物流信息'


@api.route('', methods=['PUT'])
@api.doc(args=['g.body.id','datetime','status_id','data'])
def update():
    '''修改物流信息'''
    return '修改物流信息'


@api.route('', methods=['DELETE'])
@api.doc(args=['g.body.id'])
def delete():
    '''删除物流信息'''
    return '删除物流信息'


@api.route('/list', methods=['GET'])
@api.doc()
def list():
    '''多个物流信息'''
    return '多个物流信息'
