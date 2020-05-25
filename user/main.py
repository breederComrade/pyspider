# 蓝图

from flask import Blueprint
# 定义蓝图
user = Blueprint('user', __name__)

# TODO: 视图函数在其他文件内如何导入
@user.route('/')
def index():
    return 'user_index'


# TODO:用户列表需要权限控制

@user.route('/list', methods=['post'])
def userList():
    return '用户列表'


# 创建用户
@user.route('/create')
def userCreate():
    return '用户创建'


# 删除用户
@user.route('/delete')
def userDelete():
    return '删除用户'


@user.route('/update')
def userUpdate():
    return '更新用户信息'
