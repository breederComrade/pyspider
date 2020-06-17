# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from flask import g
from app.core.error import Success
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import company as api_doc
from app.models.company import Company

api = Redprint(name='company', description='企业', api_doc=api_doc)


@api.route('', methods=['GET'])
@api.doc(args=['query.company_id'])
def get_Company():
    ''' 获取单个企业 '''
    company = Company.get_or_404(id=1)
    
    return 'diz '


@api.route('/list', methods=['GET'])
@api.doc()
def get_all_Company():
    '''查询所有「配送信息」'''
    Company_list = Company.query.filter_by(user_id=g.user.id).all_by_wrap()
    return Success(Company_list)


@api.route('', methods=['PUT'])
@api.doc(args=['company_name', 'company_id'])
def update_Company():
    '''修改企业'''
    return '修改企业'


@api.route('', methods=['DELETE'])
@api.doc(args=['company_id'])
def delete_Company():
    '''删除企业'''
    return '删除企业'


@api.route('', methods=['POST'])
@api.doc(args=['company_name'])
def create():
    '''创建企业'''
    return '创建成功'


@api.route('/add', methods=['POST'])
@api.doc(args=['g.body.uid', 'company_id'])
def add_user():
    '''添加用户'''
    return '添加用户'


# 批量添加用户
@api.route('/adds', methods=['POST'])
@api.doc()
def add_user_batch():
    '''批量添加用户'''
    return '批量添加用户'

# 删除用户
@api.route('/cancel', methods=['POST'])
@api.doc(args=['g.body.uid', 'company_id'])
def cancel_user():
    '''取消用户'''
    return '取消用户'


# 批量删除用户
@api.route('/cancels', methods=['POST'])
# TODO:批量数组处理
@api.doc(args=['g.body.uid', 'company_id'])
def cancel_user_batch():
    '''批量取消用户'''
    return '批量取消用户'
