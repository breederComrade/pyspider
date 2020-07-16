# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""


from flask import request, json

from app.core.error import Success, NotFound
from app.dao.category import  CategoryDao
from app.core.token_auth import auth
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import category as api_doc
from app.models.category import Category
from app.validators.forms import CategoryValidator, IDMustBePositiveIntValidator

api = Redprint(name='category', description='分类', api_doc=api_doc)


@api.route('', methods=['GET'])
@api.doc(args=['query.category_id'])
def get_category():
    '''获取分类'''
    id= IDMustBePositiveIntValidator().nt_data.id
    category = Category.get_or_404(id=id)
    
    
    
    
    
    # TODO:如何返回数据父类或者子类的数据
    return Success(category)

# 创建分类
@api.route('', methods=['POST'])
@api.doc(args=['category_name', 'category_parent_id','g.body.remark'])
def create():
    '''创建分类'''
    # 创建
    # 验证表单
    form = CategoryValidator().nt_data
    # 创建数据
    category = CategoryDao.create(form);
    return Success(category,error_code=1)
    

@api.route('/delete', methods=['DELETE'])
@api.doc(args=['query.category_id'])
def delete():
    '''删除分类'''
    id = IDMustBePositiveIntValidator().nt_data.id
    if not id:
        raise NotFound(msg='请查看id是否填写正确')
    CategoryDao.delete(id)
    return Success(error_code=2)

@api.route('', methods=['PUT'])
@api.doc(args=['category_id','category_name', 'category_parent_id'],auth=True)
@auth.login_required
def update():
    '''修改分类信息'''
    # 验证id
    id = IDMustBePositiveIntValidator().nt_data.id
    form = CategoryValidator().dt_data
    CategoryDao.update(id,**form)
    return Success(error_code=1)

@api.route('/list', methods=['GET'])
@api.doc()
def list():
    '''分类列表'''
    
    # 通过父id查找子分类
    category = Category.get_or_404(id=1)
    return Success(error_code=2)
