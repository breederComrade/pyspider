# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""

from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import user as api_doc

api = Redprint(name='express_company', description='物流公司', )
