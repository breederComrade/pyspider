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
from app.models.express_company import ExpressCompany

api = Redprint(name='express_company', description='物流公司', )

@api.route('', methods=['GET'])
@api.doc()
def get():
    ''' 获取单个物流公司 '''
    company = ExpressCompany.get_or_404(id=1)
    return 'diz '


@api.route('/list', methods=['GET'])
@api.doc()
def list():
    '''查询所有「物流公司信息」'''
    customer_list = ExpressCompany.query.filter_by(user_id=g.user.id).all_by_wrap()
    return Success(customer_list)


@api.route('/update', methods=['POST'])
@api.doc()
def update():
    '''修改物流公司'''
    return '修改物流公司'


@api.route('/delete', methods=['POST'])
@api.doc()
def delete():
    '''删除物流公司'''
    return '删除物流公司'


@api.route('/create', methods=['POST'])
@api.doc()
def create():
    '''创建物流公司'''
    return '创建成功'
