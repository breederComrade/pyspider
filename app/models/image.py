# _*_ coding: utf-8 _*_
"""
  Created by wangjun on 2020/06/10.
  __author__ = 'wangjun'
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db


class Image(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True, autoincrement=True)
    _url = Column('url', String(255), comment='图片路径')
    
    def __repr__(self):
        return '图片路径：{}'.format(self.url)
    
    def keys(self):
        return self.fields
    
    @property
    def url(self):
        return self.get_url(self._url)

    @staticmethod
    def get_img_by_id(id):
        return Image.query.filter_by(id=id).first_or_404()

