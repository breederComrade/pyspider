# 蓝图

from flask import Blueprint,request
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


# 用户登录
# TODO:查询数据库
@user.route('/login',methods=['POST','GET'])
def user_login():
    print(request.args)
    
    # get方式
    # account= request.args.get('account')
    # password= request.args.get('password')
    # 获取json参数
    data = request.get_json()
    password = data['password']
    account = data['account']
    # 获取form-data方式数据
    # data1_account = request.form.get('account')
    # data1_password = request.form.get('password')
    # print(data)
    
    # formdata方式使用form获得数据
    # print(data1_account)
    # print(data1_password)

    print(account)
    if(account=='admin' and password=='123'):
        return '登录成功'
    return '登录失败'


# 用户注册
# TODO:查询数据库
@user.route('/register',methods=['POST'])
def user_register():
    data = request.get_json()
    password = data['password']
    account = data['account']
    
    print('dddd',data)
    if(account=='admin' and password=='123'):
        return '注册成功'
    return '注册失败'