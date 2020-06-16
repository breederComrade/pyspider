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
from app.models.category import Category

api = Redprint(name='category', description='分类', )

@api.route('',methods=['GET'])
@api.doc()
def get_category():
    '''获取分类'''
    category = Category.get_or_404(id =1)
    return Success(error_code=2)

# 创建分类
@api.route('/create',methods=['GET'])
@api.doc()
def create():
    '''创建分类'''
    category = Category.get_or_404(id =1)
    return Success(error_code=2)


@api.route('/list',methods=['GET'])
@api.doc()
def list():
    '''分类列表'''
    category = Category.get_or_404(id =1)
    return Success(error_code=2)

@api.route('/list',methods=['GET'])
@api.doc()
def delete():
    '''删除分类'''
    category = Category.get_or_404(id =1)
    return '删除分类'


@api.route('/list',methods=['GET'])
@api.doc()
def update():
    '''修改分类信息'''
    category = Category.get_or_404(id =1)
    return '修改分类信息'

