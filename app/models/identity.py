# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/11.
  author: wangjun
  description: 身份多登陆表
  
"""
from flask import current_app
from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.core.db import EntityModel as Base
from app.libs.enums import ClientTypeEnum


class Identity(Base):
    __tablename__ = 'identity'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, comment='外键，用户id')
    '''
    登录类型：- 用户名登录(type:100)
    - 邮箱账号登录(type:101)
    - 手机账号登录(type:102)
    - 小程序登录(type:200)
    - 微信扫码登录(type:201)
    '''
    type = Column(Integer, nullable=False, comment='登录类型')
    # 唯一标识，如微信登录账号---账号登录---小程序openid 其他第三方应用
    identifier = Column(String(100), unique=True, comment='标识(手机号、邮箱、用户名或第三方应用的唯一标识)')
    
    # 密码与凭证
    _credential = Column('credential', String(100), comment='密码凭证')
    #
    verified = Column(SmallInteger, default=0, comment='是否已经通过验证')
    
    def keys(self):
        self.hide('id', 'user_id', '_credential')
        return self.fields
    
    #     登录类型名
    def name(self):
        return ClientTypeEnum(self.type).name.lower()


    @property
    def credential(self):
        return self._credential

    @credential.setter
    def credential(self, raw):
        self._credential = raw

    @property
    def password(self):
        return self._credential

    @password.setter
    def password(self, raw):
        # 站内登录方式(用户名、手机、邮箱)的密码需要加密
        if ClientTypeEnum(self.type) in current_app.config['CLINET_INNER_TYPES']:
            self._credential = generate_password_hash(raw)
        # 第三方应用的token
        else:
            self._credential = raw

    # 校验站内登录方式(用户名、手机、邮箱)
    def check_password(self, raw, e=None):
        if not self._credential:
            return False
        is_correct = check_password_hash(self._credential, raw)
        if not is_correct and e:
            raise e
        return is_correct

