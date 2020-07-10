# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/6/28
  author: wangjun
  description: 角色表
  
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base

class Role(Base):
    id = Column(Integer,primary_key=True)
    name = Column(String(25),comment='角色名称')
    company_id  = Column(Integer, ForeignKey('company.id'), comment='所属公司')
    
    # 关联权限表
    permission = relationship('Permission',secondary = 'role_permission',backref=backref('role',lazy = 'dynamic'))
    
    def __repr__(self):
        return '角色：{}'.format(self.name)
    
    def keys(self):
        return self.fields
