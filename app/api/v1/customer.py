# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from app.core.error import Success
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import user as api_doc
from app.models.customer import Customer

api = Redprint(name='customer', description='客户', )


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
    customer_list = Customer.query.filter_by(user_id=g.user.id).all_by_wrap()
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


@api.route('', methods=['POST'])
@api.doc(args=['g.body.customer_name', 'g.body.avatar', 'g.body.mobile', 'g.body.wechat', 'g.body.uid',
               'g.body.customer_company_id'])
def create():
    '''创建客户'''
    return '创建成功'
