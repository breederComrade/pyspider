# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/7/19
  author: wangjun
  description: 物流公司
  
"""

from flask import g

from app.core.db import db
from app.models.customer import Customer
from app.models.express_company import ExpressCompany


class ExpCompanyDao(object):
    @staticmethod
    def create(form):
        with db.auto_commit():
            ExpressCompany.create(
                name=getattr(form, 'name', None)
            )
    
    @staticmethod
    def update(id, **form):
        with db.auto_commit():
            expc = ExpressCompany.get_or_404()
            expc.update(**form)
    
    @staticmethod
    def delete(id):
        with db.auto_commit():
            expc = ExpressCompany.get_or_404(id = id)
            expc.delete()
    
 