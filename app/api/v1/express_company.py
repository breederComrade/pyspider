# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from flask import g

from app.core.error import Success
from app.core.utils import paginate
from app.dao.expresscompany import ExpCompanyDao
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import express_commany as api_doc
from app.models.express_company import ExpressCompany
from app.validators.forms import ExpressCompanyValidator, IDMustBePositiveIntValidator

api = Redprint(name='express_company', description='物流公司', api_doc=api_doc)


@api.route('', methods=['POST'])
@api.doc(args=['express_company_name'])
def create():
    '''创建物流公司'''
    form = ExpressCompanyValidator().nt_data
    ExpCompanyDao.create(form)
    return Success(error_code=1)


@api.route('', methods=['DELETE'])
@api.doc(args=['express_company_id'])
def delete():
    '''删除物流公司'''
    id = IDMustBePositiveIntValidator().nt_data.id
    ExpCompanyDao.delete(id)
    return Success(error_code=2)


@api.route('', methods=['PUT'])
@api.doc(args=['express_company_id', 'express_company_name', ])
def update():
    '''修改物流公司'''
    id = IDMustBePositiveIntValidator().nt_data.id
    form = ExpressCompanyValidator().dt_data
    ExpCompanyDao.update(id, **form)
    return Success(error_code=1)


@api.route('', methods=['GET'])
@api.doc(args=['g.query.id'])
def get():
    ''' 获取单个物流公司 '''
    id = IDMustBePositiveIntValidator().nt_data.id
    expc = ExpressCompany.get_or_404(id=id)
    return Success(expc)


@api.route('/list', methods=['GET'])
@api.doc(args=['g.query.page', 'g.query.size'])
def list():
    '''查询所有「物流公司信息」'''
    page, size = paginate()
    expcs = ExpressCompany.query.filter_by().paginate(page=page, per_page=size, error_out=False)
    return Success({
        'total': expcs.total,
        'current_page': expcs.page,
        'items': expcs.items
    }, )
