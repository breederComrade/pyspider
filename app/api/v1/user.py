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

api = Redprint(name='user', description='用户', api_doc=api_doc)


#
@api.route('', methods=['GET'])
@api.doc(args=['g.query.userId'])
def get_user():
    '''查询单个用户信息'''
    # get是我们自定义的方法本意是调用了fliterby
    user = User.get(id=g.user.id)
    return Success(user)


# 更改密码
@api.route('/password', methods=['GET'])
@api.doc()
def update_password():
    '''更改密码'''
    return '密码'


@api.route('/list', methods=['GET'])
@api.doc()
def user_list():
    '''用户列表'''
    return '用户列表'


# post
# 创建用户
@api.route('/create', methods=['POST'])
@api.doc(args=['account', 'password'])
def create_user():
    '''创建用户'''
    return '创建用户'


# 删除用户
@api.route('/delete', methods=['DELETE'])
@api.doc()
def del_user():
    '''删除用户'''
    return '删除用户'


# 修改用户
@api.route('/update', methods=['POST'])
@api.doc()
def update_user():
    '''更新用户信息'''
    return '修改用户'


# 更新用户头像
@api.route('/avatar', methods=['GET'])
@api.doc()
def update_avatar():
    '''更新头像'''
    return '更新用户头像'


# 解绑账号
@api.route('/unbind', methods=['unbind'])
@api.doc()
def unbind():
    '''解绑账号'''
    return '解绑帐号'
