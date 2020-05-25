
# 蓝图
from flask import Flask,Blueprint

goods = Blueprint('goods',__name__)

# 首页
@goods.route('/')
def index():
    return '货品首页'

# 列表
@goods.route('/list')
def goods_list():
    return '货品列表'

# 详情
@goods.route('/get')
def goods_get():
    return '货品详情'

# 创建
@goods.route('/create')
def goods_create():
    return '货品创建'

# 删除
@goods.route('/delete')
def goods_delete():
    return '货品delete'

# 更新
@goods.route('/update')
def goods_update():
    return '货品更新'
