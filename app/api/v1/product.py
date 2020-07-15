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
from app.core.utils import paginate, pageinateByBody, time_interval
from app.dao.product import ProductDao
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import product as api_doc
from app.models.product import Product
from app.validators.forms import CreateProductValidator, ListProductValidator, IDMustBeNaturalNumValidator, \
    IDMustBePositiveIntValidator, ProductIDValidator

api = Redprint(name='product', description='商品', api_doc=api_doc)


@api.route('', methods=['POST'])
@api.doc(args=['name', 'price', 'stocknum', 'remark', ], auth=True)
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
@api.doc(args=['g.query.product_id'], auth=True)
@auth.login_required
def get():
    ''' 获取单个商品 '''
    id = ProductIDValidator().nt_data.product_id
    product = Product.query.filter_by(id=id, user_id=g.user.id).first()
    return Success(product)

@api.route('', methods=['PUT'])
@api.doc(args=['product_id', 'name', 'price', 'stocknum', 'remark'],auth=True)
@auth.login_required
def update():
    '''修改商品'''
    # 验证表单
    id = IDMustBePositiveIntValidator().nt_data.id
    form = CreateProductValidator().dt_data
    # 操作更新
    # form 是dict数据
    ProductDao.update_product(id ,**form)
    
    return Success(error_code=1)


@api.route('/list', methods=['GET'])
# 参数分类id 是否停用 创建日期
# TODO：热销--滞销
@api.doc(args=['category_id', 'g.query.status', 'g.query.start', 'g.query.end', 'g.query.page', 'g.query.size', ],
         auth=True)
@auth.login_required
def list():
    '''查询所有「商品信息」'''
    page, size = paginate()
    start, end = time_interval()
    validator = ListProductValidator().dt_data
    categoryid = validator.get('category_id', None)
    status = validator.get('status', None)
    # 2.查询 查询符合条件的所有数据列表
    product = ProductDao.get_product_list(categoryid=categoryid, createTime=start, actives=status, page=page, size=size)
    return Success(product)
