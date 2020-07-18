# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from flask import g, json
from sqlalchemy import exists

from app.core.error import Success, ParameterException, NotFound
from app.core.token_auth import auth
from app.core.utils import paginate
from app.dao.address import AddressDao
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import address as api_doc
from app.models.address import Address
from app.models.customer import Customer
from app.validators.forms import AddressValidator, IDMustBePositiveIntValidator, AddressBaseValidator

api = Redprint(name='address', description='配送地址', api_doc=api_doc)


@api.route('', methods=['POST'])
@api.doc(args=['name', 'mobile', 'province', 'city', 'country', 'detail', 'customer', 'g.body.geender'])
def create():
    '''创建地址'''
    # 验证表单
    form = AddressValidator().nt_data
    # 开始
    AddressDao.create(form)
    return Success(error_code=1)


@api.route('', methods=['DELETE'])
@api.doc(args=['g.query.id'], auth=True)
@auth.login_required
def delete_address():
    '''删除地址'''
    # 比对用户信息
    # 连表查询
    id = IDMustBePositiveIntValidator().nt_data.id
    address = Address.get_or_404(id=id)
    if address.customer and address.customer.user_id != g.user.id:
        raise NotFound()
    address.delete()
    return Success()


@api.route('', methods=['GET'])
@api.doc(args=['g.query.id'], auth=True)
@auth.login_required
def get_address():
    ''' 获取单个地址 '''
    id = IDMustBePositiveIntValidator().nt_data.id
    
    address = Address.get_or_404(id=id)
    # 判断是否是执行自己
    if not address.customer or address.customer.user_id != g.user.id:
        raise NotFound()
    return Success(address)


@api.route('', methods=['PUT'])
@api.doc(args=['g.body.id', 'name', 'mobile', 'province', 'city', 'country', 'detail', 'customer', 'g.body.geender'],
         auth=True)
@auth.login_required
def update_address():
    '''修改地址'''
    id = IDMustBePositiveIntValidator().nt_data.id
    form = AddressBaseValidator().dt_data
    AddressDao.update_address(id, g.user.id, **form)
    return Success(error_code=1, msg='地址修改成功')


@api.route('/list', methods=['GET'])
@api.doc(args=['query.customer', 'g.query.page', 'g.query.size'], auth=True)
@auth.login_required
def list():
    '''查询所有「配送信息」'''
    # 分页
    # 获取指定客户的地址
    # 必须是这个用户的客户
    #
    
    # 1.找到
    page, size = paginate()
    #
    customerId = IDMustBePositiveIntValidator().nt_data.id
    #
    customer = Customer.query.filter_by(id=customerId, user_id=g.user.id).first()
    
    if not customer:
        raise NotFound()
    
    # 当前用户手下的客户的地址
    address = Address.query.filter_by(customer_id=customerId).paginate(
        page=page,
        per_page=size,
        error_out=False
    )
    
    return Success({
        'total': address.total,
        'current_page': address.page,
        'items': address.items
    })


@api.route('/setDefault', methods=['GET'])
@api.doc(args=['g.path.address_id'])
def set_default():
    '''设置默认地址'''
    return '设置默认地址'
