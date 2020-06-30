# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/30.
  author: wangjun
  description: 角色
"""
from app.core.error import Success
from app.core.redprint import Redprint
from app.core.token_auth import auth
from app.models.role import Role

api = Redprint(name='token', description='角色')

@api.route('',methods=['GET'])
@api.doc(args=['g.query.id'])
@auth.admin_required
def get_role():
    '''获取指定角色列表'''
    return Success()

@api.route('',methods=['POST'])
@api.doc(args=['g.query.id'])
@auth.admin_required
def post_role():
    '''新增角色'''
    return Success()

@api.route('',methods=['PUT'])
@api.doc(args=['g.query.id'])
@auth.admin_required
def post_role():
    '''修改角色'''
    return Success()


@api.route('',methods=['DELETE'])
@api.doc(args=['g.query.id'])
@auth.admin_required
def del_role():
    '''删除角色'''
    return Success()


@api.route('',methods=['PUT'])
@api.doc(args=['g.query.id'])
@auth.admin_required
def set_role_by_user():
    '''设置用户角色'''
    return Success()


@api.route('/delete',methods=['PUT'])
@api.doc(args=['g.query.id'])
@auth.admin_required
def set_role_by_user():
    '''设置用户角色'''
    role = Role.get_or_404(id=1)
    return Success()

