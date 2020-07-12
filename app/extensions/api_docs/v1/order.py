# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/17.
  author: wangjun
  description: 
  
"""
from app.core.swagger_filed import BodyField, IntegerPathFiled, IntegerQueryFiled

order_id_in_query = IntegerQueryFiled(name='id', description='订单id')

order_id_in_body = BodyField(name='id', type='integer', description='订单id')
order_code = BodyField(name='code', type='string', description='订单编码')

order_product = BodyField(name='productArr', type='array', description='订单货品', default={})

order_status_id = BodyField(name='status_id', type='integer', description='订单状态')

order_remark = BodyField(name='remark', type='string', description='订单备注')

order_total_count = BodyField(name='totalcount', type='integer', description='订单货品数量')
order_total_price = BodyField(name='totalprice', type='integer', description='订单总价')
order_pay_id = BodyField(name='pay_id', type='integer', description='订单支付单号')
