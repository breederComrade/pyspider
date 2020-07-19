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
from app.dao.customer import CustomerDao
from app.extensions.api_docs.redprint import Redprint
from app.models.customer import Customer
from app.validators.forms import CustomerValidator, IDMustBePositiveIntValidator, CustomerBaseValidator
from app.extensions.api_docs.v1 import customer as api_doc

api = Redprint(name='customer', description='客户', api_doc=api_doc)


@api.route('', methods=['POST'])
@api.doc(args=['g.body.nickname', 'g.body.avatar', 'g.body.mobile', 'g.body.wechat', 'g.body.status'], auth=True)
@auth.login_required
def create():
    '''创建客户'''
    # 验证表单
    form = CustomerValidator().nt_data
    # dao操作
    CustomerDao.create(form)
    # 如果需要返回数据 需要等添加完成后查询即可
    return Success(error_code=1)


@api.route('', methods=['PUT'])
@api.doc(args=['g.body.id', 'g.body.nickname', 'g.body.avatar', 'g.body.mobile', 'g.body.wechat', 'g.body.status'],
         auth=True
         )
@auth.login_required
def change():
    '''修改客户ces '''
    id = IDMustBePositiveIntValidator().nt_data.id
    form = CustomerBaseValidator().dt_data
    # 更新
    CustomerDao.update(id, 9, **form)
    
    return Success(error_code=1)


@api.route('', methods=['DELETE'])
@api.doc(args=['g.query.id'], auth=True)
@auth.login_required
def delete_customer():
    '''删除客户'''
    id = IDMustBePositiveIntValidator().nt_data.id
    customer = Customer.get_or_404(id=id)
    customer.delete()
    return Success()


@api.route('', methods=['GET'])
@api.doc(args=['g.query.customer_id'], auth=True)
@auth.login_required
def get_customer():
    ''' 获取单个客户 '''
    id = IDMustBePositiveIntValidator().nt_data.id
    customer = Customer.get_or_404(id=id, user_id=g.user.id)
    return Success(customer)


@api.route('/list', methods=['GET'])
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.login_required
def get_all_customer():
    '''查询所有「客户信息」'''
    
    page, size = paginate()
    customers = Customer.query.filter_by(user_id = g.user.id).paginate(
        page=page,
        per_page=size,
        error_out=False
    )
    return Success({
        'total': customers.total,
        'current_page': customers.page,
        'items': customers.items
    })
