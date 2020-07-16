# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/07/16.
  author: wangjun
  description: 分类操作
  
"""
from app.core.db import db
from app.core.error import Failed
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
            if hasattr(form, 'category_parent_id'):
            #     判断父类是否存在
                Category.get_or_404(id = form.category_parent_id,msg='父id不存在,请检查category_parent_id值')
            # 判断是否存在
            Category.create(
                commit=False,
                name=getattr(form, 'category_name', None),
                parent_id=getattr(form, 'category_parent_id', None),
                remark=getattr(form, 'remark', ''),
            )
    
    # 删除
    @staticmethod
    def delete(id):
        '''删除分类'''
        # 删除分类并删除其子分类或修改或修改其子分类
        # 判断分类id是否存在
        category = Category.get_or_404(id=id)
        # 查询是否有子类
        print(category)
        if category.child is not None:
            raise Failed(msg='有子级分类存在 请先删除子级分类')
        # 删除相关的所有子外键
        category.delete()
    
    # 更新
    def update(self):
        pass
    
    # 获取列表
    def list(selfs):
        pass
    
    # 获取详情
    def detail(self):
        pass
