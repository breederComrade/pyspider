# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/17.
  author: wangjun
  description: 公司字段
  
"""
from app.core.swagger_filed import BodyField,IntegerQueryFiled
company_id_in_query = IntegerQueryFiled(name='id',description='企业id')
company_id = BodyField(name='id',type='string',description='企业id')
company_name = BodyField(name='name',type='string',description='企业名称')
