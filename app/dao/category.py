# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/07/16.
  author: wangjun
  description: 分类操作
  
"""
from app.core.db import db
from app.models.category import Category


class CategoryDao(object):
    # 创建
    @staticmethod
    def create(form):
        # 自动提交并保持
        with db.auto_commit():
   
            
            # 判断重复
            if hasattr(form, 'category_name'):
                Category.abort_repeat(name=form.category_name, msg='该分类已被使用，请重新输入新的分类')
            # 判断是否存在
            Category.create(
                commit=False,
                name=getattr(form, 'category_name', None),
                parent_id=getattr(form, 'category_parent_id', None),
                remark=getattr(form, 'remark', ''),
            )
    
    # 删除
    def delete(self):
        pass
    
    # 更新
    def update(self):
        pass
    
    # 获取列表
    def list(selfs):
        pass
    
    # 获取详情
    def detail(self):
        pass
