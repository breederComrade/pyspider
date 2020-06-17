# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/17.
  author: wangjun
  description: 物流公司参数
  
"""
from app.core.swagger_filed import BodyField

express_company_id_in_query = BodyField(name='id',type='integer',description='物流公司id')
express_company_id = BodyField(name='id',type='integer',description='物流公司id')

express_company_name = BodyField(name='express_company_name',type='integer',description='物流公司名称')

express_company_des = BodyField(name='express_company_des',type='integer',description='物流公司备注')

