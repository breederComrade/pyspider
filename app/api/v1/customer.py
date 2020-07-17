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
from app.dao.customer import CustomerDao
from app.extensions.api_docs.redprint import Redprint
from app.models.customer import Customer
from app.validators.forms import CustomerValidator
from app.extensions.api_docs.v1 import customer as api_doc
api = Redprint(name='customer', description='客户',api_doc=api_doc )

@api.route('', methods=['POST'])
@api.doc(args=['g.body.nickname', 'g.body.avatar', 'g.body.mobile', 'g.body.wechat','g.body.status'],auth=True)
@auth.login_required
def create():
    '''创建客户'''
    # 验证表单
    form = CustomerValidator().nt_data
    # dao操作
    CustomerDao.create(form)
    return Success()


@api.route('', methods=['GET'])
@api.doc(args=['g.query.customer_id'])
def get_customer():
    ''' 获取单个客户 '''
    company = Customer.get_or_404(id=1)
    return 'diz '


@api.route('/list', methods=['GET'])
@api.doc()
def get_all_customer():
    '''查询所有「客户信息」'''
    customer_list = Customer.query.all(user_id=g.user.id).all_by_wrap()
    return Success(customer_list)


@api.route('', methods=['PUT'])
@api.doc(
    args=['g.body.customer_id', 'g.body.customer_name', 'g.body.avatar', 'g.body.mobile', 'g.body.wechat', 'g.body.uid',
          'g.body.customer_company_id'])
def update_customer():
    '''修改客户'''
    return '修改客户'


@api.route('', methods=['DELETE'])
@api.doc(args=['g.body.customer_id'])
def delete_customer():
    '''删除客户'''
    return '删除客户'

