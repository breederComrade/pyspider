# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from app.core.error import Success
from app.dao.category import  CategoryDao
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import category as api_doc
from app.models.category import Category
from app.validators.forms import CategoryValidator

api = Redprint(name='category', description='分类', api_doc=api_doc)


@api.route('', methods=['GET'])
@api.doc(args=['g.query.category_id'])
def get_category():
    '''获取分类'''
    category = Category.get_or_404(id=1)
    return Success(error_code=2)


# 创建分类
@api.route('', methods=['POST'])
@api.doc(args=['category_name', 'category_parent_id','g.body.remark'])
def create():
    '''创建分类'''
    # 创建
    # 验证表单
    form = CategoryValidator().nt_data
    # 更新数据
    category = CategoryDao.create(form);
    return Success(category,error_code=1)
    

@api.route('/delete', methods=['DELETE'])
@api.doc(args=['category_id'])
def delete():
    '''删除分类'''
    category = Category.get_or_404(id=1)
    return '删除分类'


@api.route('', methods=['PUT'])
@api.doc(args=['category_id','category_name', 'category_parent_id'])
def update():
    '''修改分类信息'''
    category = Category.get_or_404(id=1)
    return '修改分类信息'

@api.route('/list', methods=['GET'])
@api.doc()
def list():
    '''分类列表'''
    
    # 通过父id查找子分类
    category = Category.get_or_404(id=1)
    return Success(error_code=2)
