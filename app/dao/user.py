# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/6/14
  author: wangjun
  description: 用户表操作
  
"""
from app.core.db import db
from app.models.user import User


class UserDao():
    #     更新
    def change_password(self):
        pass
    
    # 创建
    @staticmethod
    def create_user(form):
        with db.auto_commit():
            user = User.create(
                commit=False,
                nickname='fuck'
            )
        
        #  检测是否存在
        #  手机号是否使用
        #  邮箱是否使用
