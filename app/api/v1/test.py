# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/16.
  author: wangjun
  description: 测试用
  
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import test as api_doc

api = Redprint(name='test', description='测试用', api_doc=api_doc)


@api.route('', methods=['GET'])
@api.doc(args=['body.type'])
def get():
    '''获取'''
    return '获取'


@api.route('', methods=['POST'])
@api.doc()
def create():
    '''新增'''
    return '新增'


@api.route('', methods=['PUT'])
@api.doc()
def update():
    '''更新'''
    return '更新'


@api.route('', methods=['DELETE'])
@api.doc()
def delete():
    '''删除'''
    return '删除'


@api.route('/list', methods=['GET'])
@api.doc()
def list():
    '''列表'''
    return 'list'
