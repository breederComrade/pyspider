# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/07/17.
  author: wangjun
  description: 规格
  
"""

from app.core.error import Success
from app.core.utils import paginate
from app.dao.spec import SpecDao
from app.extensions.api_docs.redprint import Redprint
from app.core.token_auth import auth
from app.models.role import Role
from app.models.specifica import Specifica
from app.extensions.api_docs.v1 import spec as api_doc
from app.validators.forms import SpecValidator, IDMustBePositiveIntValidator, ProductIDValidator, UpdateSpecValidator

api = Redprint(name='spec', description='规格', api_doc=api_doc)


@api.route('', methods=['GET'])
@api.doc(args=['g.query.id'], auth=True)
@auth.login_required
def get():
    '''获取规格'''
    id = IDMustBePositiveIntValidator().nt_data.id
    spec = SpecDao.get(id)
    return Success(spec)


@api.route('', methods=['POST'])
@api.doc(args=['product_id', 'name', 'price', 'stock'], auth=True)
@auth.login_required
def create():
    '''新增规格'''
    form = SpecValidator().nt_data
    SpecDao.create(form)
    return Success(error_code=1)


@api.route('', methods=['DELETE'])
@api.doc(args=['g.query.id'], auth=True)
@auth.login_required
def delete():
    '''删除规格'''
    id = IDMustBePositiveIntValidator().nt_data.id
    SpecDao.delete(id)
    return Success(error_code=2)


@api.route('', methods=['PUT'])
@api.doc(args=['g.body.id', 'name', 'price', 'stock'], auth=True)
@auth.login_required
def update():
    '''修改规格'''
    id = IDMustBePositiveIntValidator().id.data
    form = UpdateSpecValidator().dt_data
    SpecDao.update(id,**form)
    
    return Success()

@api.route('/list', methods=['GET'])
@api.doc(args=['g.query.page', 'g.query.size', 'g.query.product_id'], auth=True)
@auth.login_required
def list():
    '''获取规格列表'''
    page, size = paginate()
    id = ProductIDValidator().nt_data.product_id
    specs = SpecDao.list(id, page, size)
    return Success(specs)
