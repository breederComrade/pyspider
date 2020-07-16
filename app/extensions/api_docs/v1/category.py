# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/17.
  author: wangjun
  description: 分类
  
"""
from app.core.swagger_filed import BodyField, IntegerQueryFiled

# id
category_id = BodyField(name='category_id', type='integer', description='商品分类id')
category_id_in_query =  IntegerQueryFiled(
    name='id', description="分类id", required=True)
category_parent_id = BodyField(name='category_parent_id', type='integer', description='商品分类上级id')
category_name = BodyField(name='category_name', type='string', description='商品分类名称')
