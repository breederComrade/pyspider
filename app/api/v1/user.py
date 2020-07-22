# _*_ coding: utf-8 _*_
"""
  created by wangjun on 2020/06/10.
  author: wangjun
  project:有单生意
  description:  用户接口
  
"""
#
from json import dump

from flask import g, request, json

from app.core.error import Success
from app.core.token_auth import auth
from app.dao.user import UserDao
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import user as api_doc
from app.models.user import User
from app.validators.forms import CreateUserValidator

api = Redprint(name='user', description='用户', api_doc=api_doc)


#
@api.route('', methods=['GET'])
@api.doc(args=['g.query.id'])
# @auth.login_required
def get_user():
    '''查询单个用户信息'''
    # get是我们自定义的方法本意是调用了fliterby
    user = User.query.get(2)
    return Success(user)


#
@api.route('/my', methods=['GET'])
@api.doc(auth=True)
@auth.login_required
def get_my():
    '''查询当前用户'''
    user = User.get_or_404(id = g.user.id)
    return Success(user)

# 更改密码
@api.route('/password', methods=['GET'])
@api.doc()
def update_password():
    '''更改密码'''
    return '密码'

# post
# 创建用户
@api.route('', methods=['POST'])
@api.doc(args=['g.body.username', 'g.body.email', 'g.body.mobile', 'g.body.nickname', 'g.body.password',
               'g.body.confirm_password'])
def create_user():
    '''创建用户'''
    # 验证数据是否正确 通过wtform
    form = CreateUserValidator().nt_data
    # 验证完成后调用Dao操作创建用户
    UserDao.create_user(form)
    return Success(error_code=1)


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

@api.route('/auths', methods=['GET'])
@api.doc(auth=True)
@auth.login_required
def get_auths():
    '''查询自己拥有的权限'''
    return Success()

#

