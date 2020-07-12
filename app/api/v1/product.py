# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 商品
  
"""
from flask import g, request

from app.core.error import Success, NotFound
from app.core.token_auth import auth
from app.dao.product import ProductDao
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import product as api_doc
from app.models.product import Product
from app.validators.forms import CreateProductValidator

api = Redprint(name='product', description='商品', api_doc=api_doc)


@api.route('', methods=['POST'])
@api.doc(args=['name', 'price', 'stocknum', 'remark', ],auth=True)
@auth.login_required
def create():
    '''创建商品'''
    # TODO：数组在文档中的使用
    # 1.验证表单
    form = CreateProductValidator().nt_data
    # # 2.创建操作e
    product = ProductDao.create_product(form)
    return Success(error_code=1, msg='创建成功')


@api.route('', methods=['DELETE'])
@api.doc(args=['g.query.product_id'], auth=True)
@auth.login_required
def delete():
    '''删除商品'''
    # 1。获取id
    id = request.args.get('product_id')
    print('xxx', id)
    if not id:
        raise NotFound(msg='请查看id是否填写')
    ProductDao.delete_product(id)
    return Success(error_code=2)


@api.route('', methods=['GET'])
@api.doc(args=['g.query.product_id'])
def get():
    ''' 获取单个商品 '''
    return Success()


@api.route('', methods=['PUT'])
@api.doc(args=['product_id', 'name', 'price', 'stocknum', 'remark'])
def update():
    '''修改商品'''
    return '修改商品'


@api.route('/list', methods=['GET'])
@api.doc()
def list():
    '''查询所有「商品信息」'''
    customer_list = Product.query.filter_by(user_id=g.user.id).all_by_wrap()
    
    return Success(customer_list)


@api.route('/product_category', methods=['GET'])
@api.doc(args=['g.query.id'])
def product_by_category():
    '''查询类别下的产品'''
    #  1.获取id
    #  2.查找分类id下的商品
    #  3.返回商品
    return Success()
