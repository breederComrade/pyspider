# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from app.core.error import Success
from app.core.token_auth import auth
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import category as api_doc
from app.models.category import Category

api = Redprint(name='category', description='分类', api_doc=api_doc)

@api.route('', methods=['GET'])
@api.doc(args=['g.query.category_id'], auth=True)
@auth.login_required
def get_category():
    '''获取分类'''
    category = Category.get_or_404(id=1)
    return Success(error_code=2)


# 创建分类
@api.route('', methods=['POST'])
@api.doc(args=['category_name', 'category_parent_id'], auth=True)
@auth.login_required
def create():
    '''创建分类'''
    category = Category.get_or_404(id=1)
    # 分类名字
    # 分类备注
    
    
    return Success()


@api.route('/delete', methods=['DELETE'])
@api.doc(args=['category_id'], auth=True)
@auth.login_required
def delete():
    '''删除分类'''
    category = Category.get_or_404(id=1)
    return '删除分类'


@api.route('', methods=['PUT'])
@api.doc(args=['category_id', 'category_name', 'category_parent_id'], auth=True)
@auth.login_required
def update():
    '''修改分类信息'''
    category = Category.get_or_404(id=1)
    return '修改分类信息'


@api.route('/list', methods=['GET'])
@api.doc(args=['g.query.id'], auth=True)
@auth.login_required
def list():
    '''分类列表'''
    category = Category.get_or_404(id=1)
    return Success(error_code=2)
