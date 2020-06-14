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
from app.models.company import Company

api = Redprint(name='company', description='企业', )

@api.route('',methods=['GET'])
@api.doc()
def get_company():
    commany = Company.get_or_404(id=1)
    return Success(error_code=2)