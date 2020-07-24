# _*_ coding: utf-8 _*_
"""
  Created by wangjun on 2020/06/10.
  __author__ = 'wangjun'
    description: 用户组

  
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True, comment='权限组名称')
    info = Column(String(255), comment='权限组描述')
    user = relationship('User', secondary='user_group', backref=backref('user', lazy='dynamic'))
    # 用户组表 多对多
    user = relationship('User', secondary='user_group', backref=backref('group_user', lazy='dynamic'))
    
    # 关联角色
    role = relationship('Role', secondary='group_role', backref=backref('group_role', lazy='dynamic'))
    # 关联权限表
    permission = relationship('Permission', secondary='group_permission', backref=backref('group_perm', lazy='dynamic'))
