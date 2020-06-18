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
from app.dao.user import UserDao
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import user as api_doc
from app.models.user import User
from app.validators.forms import CreateUserValidator

api = Redprint(name='user', description='用户', api_doc=api_doc)


#
@api.route('', methods=['GET'])
@api.doc(args=['g.query.id'])
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
@api.doc(args=['g.body.username', 'g.body.email', 'g.body.mobile', 'g.body.nickname', 'g.body.password',
               'g.body.confirm_password'])
def create_user():
    '''创建用户'''
    form = CreateUserValidator().nt_data
    UserDao.create_user(form)
    return Success(error_code=1)
# 删除用户
@api.route('/batchDel', methods=['DELETE'])
@api.doc(args=['g.body.id'])
def barch_del_user():
    '''删除用户'''
    return '删除用户'


# 批量删除用户
@api.route('/BatchDelete', methods=['DELETE'])
@api.doc(args=['g.body.user_ids'])
def batch_del_user():
    '''批量删除用户'''
    return '批量删除用户'


# 注销用户---退出用户
@api.route('/layout', methods=['DELETE'])
@api.doc(args=['g.body.id'])
def layout():
    '''注销本人用户'''
    return '注销用户成功'


# 修改用户
@api.route('/update', methods=['POST'])
@api.doc(args=['g.body.id', 'g.body.username', 'g.body.email', 'g.body.mobile', 'g.body.avatar', 'g.body.nickname',
               'g.body.password', 'g.body.confirm_password'])
def update_user():
    '''更新用户信息'''
    return '修改用户'


# 更新用户头像
@api.route('/avatar', methods=['GET'])
@api.doc(args=['g.body.id', 'g.body.avatar'])
def update_avatar():
    '''更新头像'''
    return '更新用户头像'


# 解绑账号
@api.route('/unbind', methods=['PUT'])
@api.doc(args=['g.body.id'])
def unbind():
    '''解绑账号'''
    return '解绑帐号'
