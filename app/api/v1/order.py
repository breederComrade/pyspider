# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from flask import g

from app.core.error import Success
from app.core.token_auth import auth
from app.core.utils import paginate
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import order as api_doc
from app.models.m2m import OrderProduct
from app.models.order import Order
from app.validators.forms import IDMustBePositiveIntValidator

api = Redprint(name='order', description='订单', api_doc=api_doc)


@api.route('', methods=['GET'])
@api.doc(args=['query.order_id'], auth=True)
@auth.login_required
def get():
    ''' 获取单个订单 '''
    id = IDMustBePositiveIntValidator().nt_data.id
    order = Order.query.filter_by(id=id, user_id=g.user.id).first()
    return Success(order)


@api.route('/list', methods=['GET'])
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.login_required
def list():
    '''查询所有「订单信息」'''
    page, size = paginate()
    orders = Order.query.filter_by(user_id=g.user.id).paginate(
        page=page,
        per_page=size,
        error_out=False
    )
    return Success()


@api.route('', methods=['PUT'])
@api.doc(args=['body.order_id', 'order_code', 'order_product', 'order_status_id', 'order_remark', 'order_total_count',
               'order_total_price', 'order_pay_id'], auth=True)
@auth.login_required
def update():
    '''修改订单'''
    #
    return '修改订单'


@api.route('', methods=['DELETE'])
@api.doc(args=['query.order_id'], auth=True)
@auth.login_required
def delete():
    '''删除订单'''
    id = IDMustBePositiveIntValidator().nt_data.id
    order = Order.query.filter_by(id=id, user_id=g.user.id).first()
    order.delete()
    return Success(error_code=2)


@api.route('/create', methods=['POST'])
@api.doc(args=['order_code', 'order_product', 'order_status_id', 'order_remark', 'order_total_count',
               'order_total_price', 'order_pay_id'], auth=True)
@auth.login_required
def create():
    '''创建订单'''
    
    return '创建成功'


# 退货
@api.route('/return', methods=['PUT'])
@api.doc(args=['body.order_id', 'order_product'], auth=True)
@auth.login_required
def return_product():
    '''退货'''
    
    return '退货成功'
