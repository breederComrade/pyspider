
# 蓝图
from flask import Flask,Blueprint

client = Blueprint('client',__name__)

# 首页
@client.route('/')
def index():
    return '客户首页'

# 列表
@client.route('/list')
def client_list():
    return '客户列表'

# 详情
@client.route('/get')
def client_get():
    return '客户详情'

# 创建
@client.route('/create')
def client_create():
    return '客户创建'

# 删除
@client.route('/delete')
def client_delete():
    return '客户delete'

# 更新
@client.route('/update')
def client_update():
    return '客户更新'
