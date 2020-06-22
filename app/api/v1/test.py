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
from app.dao.user import UserDao
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import test as api_doc
from app.models.company import Company
from app.models.customer import Customer
# from app.models.m2m import user_company
from app.models.m2m import user_company
from app.models.order import Order
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
    # 反向 多查一
    customer = Customer.get_or_404(id=3)


@api.route('/m2m', methods=['GET'])
@api.doc(args=['g.query.id'])
def get_m2m():
    '''获取'''
    # 1.新增
    
    # 多对多关联 查询
    
    # 正向 搜索用户所属的企业
    # user = User.query.get(1)
    # print(json.dumps(user.company))
    # 反向
    # company = Company.query.get(1)
    # print(json.dumps(company.user.all()))
    # return Success(error_code=1)


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
@api.doc(args=['g.query.page', 'g.query.size'])
def list():
    '''列表 分页处理'''
    # 获取
    page = request.args.get('page')
    size = request.args.get('size')
    paginator = User.query.filter(User.nickname.startswith('user')).order_by(User.create_time.desc()).paginate(page=int(page), per_page=int(size), error_out=True)
    paginator.hide('account')
    return {
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
    }


@api.route('/oneToone', methods=['GET'])
@api.doc()
def oneToone():
    # 1. 一对一
    user = User.get_or_404(id=3)
    # order = Order()
    # order.order_no = 'pro'
    # order.order_status=1
    # db.session.add(order)
    # user.order.append(order)
    # db.session.commit()
    # 2. 正向查询
    print(json.dumps(user.order))
    # 3.反向查询
    order = Order.get_or_404(id=15)
    print(json.dumps(order.user))
    return 'xxx'
