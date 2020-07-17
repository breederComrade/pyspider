# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from flask import g
from app.core.error import Success
from app.dao.address import AddressDao
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import address as api_doc
from app.models.address import Address
from app.validators.forms import AddressValidator

api = Redprint(name='address', description='配送地址', api_doc=api_doc)


@api.route('', methods=['POST'])
@api.doc(args=['name','mobile', 'province', 'city', 'country', 'detail','customer','g.body.geender'])
def create():
    '''创建地址'''
    # 验证表单
    form = AddressValidator().nt_data
    # 开始
    AddressDao.create(form)
    return Success(error_code=1)


@api.route('', methods=['GET'])
@api.doc(args=['g.query.address_id'])
def get_address():
    ''' 获取单个地址 '''
    address = Address.get_or_404(id=1)
    return Success(address)


@api.route('/list', methods=['GET'])
@api.doc()
def list():
    '''查询所有「配送信息」'''
    address_list = Address.query.filter_by(user_id=g.user.id).all_by_wrap()
    return Success(address_list)


@api.route('/update', methods=['POST'])
@api.doc(args=['g.path.address_id', 'name', 'mobile', 'province', 'city', 'country', 'detail', 'customer'])
def update_address():
    '''修改地址'''
    return '修改地址'


@api.route('/setDefault', methods=['GET'])
@api.doc(args=['g.path.address_id'])
def set_default():
    '''设置默认地址'''
    return '设置默认地址'


@api.route('/delete', methods=['DELETE'])
@api.doc(args=['g.path.address_id'])
def delete_address():
    '''删除地址'''
    return '删除地址'
