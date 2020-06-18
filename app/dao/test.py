# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/18.
  author: wangjun
  description: 测试
  
"""
from app.core.db import db
from app.models.test import Test


class TestDao():
    #  创建
    @staticmethod
    def create(name):
        with db.auto_commit():
            test = Test.create(commit=False,name=name)
    
    #  修改
    @staticmethod
    def update(tid,name):
        test = Test.get_or_404(id=tid)
        test.name = name
        with db.auto_commit():
            test.update()
    
    #  删除
    @staticmethod
    def delete(userid):
        test = Test.get_or_404(id=userid)
        with db.auto_commit():
            test.hard_delete(commit=False)
        
    # 列表
    @staticmethod
    def list():
        pass
