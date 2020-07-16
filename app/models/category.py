# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/6/14
  author: wangjun
  description: 
  
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db
from app.libs.error_code import CategoryException


class Category(Base):
    '''商品类别'''
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, comment='名称')
    remark = Column(String(100), nullable=False,comment='描述')
    # # 外键关联
    parent_id = Column(Integer, ForeignKey('category.id'))
    # # 一对多关联父分类
    child = relationship("Category", back_populates="parents")
    parents = relationship('Category', back_populates='child', remote_side=[id])
    
    def keys(self):
        return self.fields
    
    @staticmethod
    def get_all_categories():
        return Category.query.all_or_404(e=CategoryException, wrap='items')
