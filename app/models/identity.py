# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/11.
  author: wangjun
  description: 身份多登陆表
  
"""
from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger

from app.core.db import EntityModel as Base


class Identity(Base):
    __tablename__='identity'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'),nullable=False,comment='外键，用户id')
    '''
    登录类型：- 用户名登录(type:100)
    - 邮箱账号登录(type:101)
    - 手机账号登录(type:102)
    - 小程序登录(type:200)
    - 微信扫码登录(type:201)
    '''
    type = Column(Integer,nullable=False,comment='登录类型')
    # 唯一标识，如微信登录账号---账号登录---小程序openid 其他第三方应用
    identity = Column(String(100), unique=True, comment='标识')
    
    # 密码与凭证
    _credential = Column('credential',String(100), comment='密码凭证')
    
    verified = Column(SmallInteger, default=0, comment= '是否已经通过验证')
    
    def keys(self):
        return self.fields
    
    
    

    
    
    

