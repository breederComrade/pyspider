# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/6/14
  author: wangjun
  description: 用户表操作
  
"""
from app.core.db import db
from app.libs.enums import ScopeEnum, ClientTypeEnum
from app.models.identity import Identity
from app.models.user import User


class UserDao():
    # 修改密码
    @staticmethod
    def change_password(self):
        pass
    # 重置密码
    @staticmethod
    def reset_password(uid,password):
        pass
    # 站内注册
    @staticmethod
    def create_user(form):
        pass
    
    # 小程序注册
    @staticmethod
    def register_by_wx_mina(openid:str):
        pass
    
    
    # 微信第三方注册
    @staticmethod
    def register_by_wx_open(form):
        pass
    
    # 微信账号注册
    @staticmethod
    def register_by_wx_account():
        pass
    
    # 更新用户
    @staticmethod
    def update_user(uid,form):
        pass
    
    # 设置头像
    @staticmethod
    def set_avatar(id,avatar):
        '''
        
        :param id: 用户id
        :param avatar: 头像url
        :return:
        '''
        
        pass
    
    # 删除用户
    @staticmethod
    def delete_user():
        pass
    
    
    # 更换权限组
    @staticmethod
    def change_group(uid, group_id):
        pass
    
    
    
    
    
    
    # 创建
    @staticmethod
    def create_user(form):
        # 主动提交
        with db.auto_commit():
            # 1.通过form创建用户model
            user = User.create(
                commit=False,
                nickname=getattr(form, 'nickname', None),
                auth=ScopeEnum.COMMON.value
            )
            
            # 2.判断form中出现指定的关键indetity身份
            # 多登陆方式支持的用户名 手机 email
            # 每个验证都需要判断是否已经存在 已经存在抛出异常
            if (hasattr(form, 'username')):
                # 验证是否有重复的
                Identity.abort_repeat(identifier=form.username, msg='该用户名已被使用，请重新输入新的用户名')
                # 创建用户身份
                Identity.create(commit=False, user_id=user.id, type=ClientTypeEnum.USERNAME.value, verified=1,
                                identifier=form.username, password=form.password)
            if (hasattr(form, 'mobile')):
                Identity.abort_repeat(identifier=form.mobile, msg='手机号已被使用，请重新输入新的手机号')
                Identity.create(commit=False, user_id=user.id, type=ClientTypeEnum.MOBILE.value,
                                identifier=form.mobile, password=form.password)
            if (hasattr(form, 'email')):
                Identity.abort_repeat(identifier=form.email, msg='邮箱已被使用，请重新输入新的邮箱号')
                Identity.create(commit=False, user_id=user.id, type=ClientTypeEnum.EMAIL.value,
                                identifier=form.email, password=form.password)
      #   修改密码
      
      