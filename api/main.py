# api接口
from flask import Flask, Blueprint

api = Blueprint('api', __name__)


# 文档首页
@api.route('/')
def index():
    return 'Swagger--api首页'


# 商品
@api.route('/goods')
def get():
    return '货品列表'


# 商品详情
@api.route('/goods/<int:id>')
def goods_get(id):
    return '货品：goodsId'


# 商品新增
@api.route('/goods/create')
def goods_create():
    return '新增货品'


# 商品修改
@api.route('/goods/update')
def goods_update():
    return '更新货品'


# 商品删除
@api.route('/goods/delete')
def goods_delete():
    return '删除货品'

# 客户


# 用户


# 物流


#
