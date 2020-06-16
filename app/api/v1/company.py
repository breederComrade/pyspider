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
from app.models.company import Company

api = Redprint(name='company', description='企业', )




@api.route('', methods=['GET'])
@api.doc()
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


@api.route('/update', methods=['POST'])
@api.doc()
def update_Company():
    '''修改企业'''
    return '修改企业'


@api.route('/setDefault', methods=['POST'])
@api.doc()
def set_default():
    '''设置默认企业'''
    return '设置默认企业'


@api.route('/delete', methods=['POST'])
@api.doc()
def delete_Company():
    '''删除企业'''
    return '删除企业'


@api.route('/create', methods=['POST'])
@api.doc()
def create():
    '''创建企业'''
    return '创建成功'
