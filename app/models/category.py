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
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, comment='名称')
    desc = Column(String(100), comment='描述')
    topic_img_id = Column(Integer, ForeignKey('image.id'), comment='外键,关联image表 ')
    image = relationship('Image', backref=backref('category', lazy='dynamic'))
    
    def keys(self):
        return self.fields

    @staticmethod
    def get_all_categories():
        return Category.query.all_or_404(e=CategoryException, wrap='items')
