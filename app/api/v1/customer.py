# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""

from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import user as api_doc
from app.models.customer import Customer

api = Redprint(name='customer', description='客户', )

@api.route()
@api.doc()
def get_customer():
    customer = Customer.get_or_404(id = 1)
    
    return '客户'