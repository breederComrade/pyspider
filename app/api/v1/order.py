# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""

from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import user as api_doc
from app.models.order import Order

api = Redprint(name='order', description='订单', )

@api.route()
@api.doc()
def get_order():
    order = Order.get_or_404(id=1)
    return '订单'