# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/16.
  author: wangjun
  description: 测试用
  
"""
from flask import request, json

from app.core.db import db
from app.core.error import Success, Failed
from app.dao.test import TestDao
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import test as api_doc
from app.models.customer import Customer
from app.models.test import Test
from app.models.user import User

api = Redprint(name='test', description='测试用', api_doc=api_doc)


@api.route('', methods=['GET'])
@api.doc(args=['g.query.id'])
def get():
    '''获取'''
    # 正向 一查多 通过用户查找该用户所属客户
    id = request.args.get('id')
    user = User.get_or_404(id=id).customer
    # 反向
    customer = Customer.get_or_404(id=3)
    return Success(customer,error_code=1)


@api.route('', methods=['POST'])
@api.doc(args=['name'])
def create():
    '''新增'''
    name = request.json.get('name')
    Test.create(name)
    return Success(error_code=1)


@api.route('', methods=['PUT'])
@api.doc(args=['id', 'name'])
def update():
    '''更新'''
    id = request.json.get('id')
    name = request.json.get('name')
    TestDao.update(id, name)
    return Success(error_code=1)


@api.route('', methods=['DELETE'])
@api.doc(args=['id'])
def delete():
    '''删除'''
    #
    id = request.json.get('id')
    TestDao.delete(id)
    return Success(error_code=2)


@api.route('/list', methods=['GET'])
@api.doc()
def list():
    '''列表'''
    return 'list'
