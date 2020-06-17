# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 商品
  
"""
from flask import g

from app.core.error import Success
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import product as api_doc
from app.models.product import Product

api = Redprint(name='product', description='商品', api_doc=api_doc)


@api.route('', methods=['GET'])
@api.doc(args=['g.query.product_id'])
def get():
    ''' 获取单个商品 '''
    company = Product.get_or_404(id=1)
    return 'diz '


@api.route('/list', methods=['GET'])
@api.doc()
def list():
    '''查询所有「商品信息」'''
    customer_list = Product.query.filter_by(user_id=g.user.id).all_by_wrap()
    return Success(customer_list)


@api.route('', methods=['PUT'])
@api.doc(args=['product_id', 'name', 'price', 'stocknum', 'remark', 'imgs'])
def update():
    '''修改商品'''
    return '修改商品'


@api.route('', methods=['DELETE'])
@api.doc(args=['g.query.product_id'])
def delete():
    '''删除商品'''
    return '删除商品'


@api.route('/create', methods=['POST'])
@api.doc(args=['name', 'price', 'stocknum', 'remark', 'imgs'])
def create():
    '''创建商品'''
    return '创建成功'
