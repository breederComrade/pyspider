# _*_ coding: utf-8 _*_
"""
  created by wangjun on 2020/06/10.
  author: wangjun
  project:有单生意
  description:  用户接口
  
"""
#
from flask import g

from app.core.error import Success
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import user as api_doc
from app.models.user import User

api = Redprint(name='user', description='用户', )


#
@api.route('', methods=['GET'])
def get_user():
    # get是我们自定义的方法本意是调用了fliterby
    user = User.get(id=g.user.id)
    return Success(user)

# get
# @api.route('/get',methods=['GET'])
# @api.doc()
# def call_user():
#     return '获取用户'

# post
# 创建用户
@api.route('/create',methods = ['POST'])
@api.doc(args=['g.body.username', 'g.body.email', 'g.body.mobile', 'g.body.nickname',
               'g.body.password', 'g.body.confirm_password'])
def create_user():
    return '创建用户'
# 删除用户
@api.route('/delete',methods = ['DELETE'])
@api.doc()
def del_user():
    return '删除用户'

# 修改用户
@api.route('/update',methods=['POST'])
@api.doc()
def update_user():
    return '修改用户'
