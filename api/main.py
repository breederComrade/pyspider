# api接口
import json

from flask import Flask, Blueprint, request,current_app

from app.extension import db
from app.models import GoodsModel,UseModel,AddressModel,CustomerModel,ExpressModel,OrderGoodsModel,OrderModel

api = Blueprint('api', __name__)

#

# 文档首页
@api.route('/')
def index():
    # current_app.logger.error('error')
    # current_app.logger.warn('warn')
    # current_app.logger.info('info')
    # current_app.logger.debug('debug')
    return 'Swagger--api首页'


# 商品
@api.route('/goods')
def get():
   
    
    # 序列化
    
    
    return '货品列表'


# 商品详情
@api.route('/goods/<int:id>')
def goods_get(id):
    goods = GoodsModel.query.filter_by(id=id).first()
    print(goods.name)
    return '货品：goodsId'


# 商品新增
@api.route('/goods/create')
def goods_create():
    # 数据库中查找
    goods = GoodsModel(name='垃圾', num=12)
    db.session.add(goods)
    db.session.commit()
    return '新增货品成功'


# 商品修改
@api.route('/goods/update', methods=['POST'])
def goods_update():
    # 获取json参数
    # name = request.json.get("name")
    # print('name:${name}')
    #  content-type = appliction/json
    n = request.get_json().get('name')
    print(n)
    # 更新方式一
    # goods = GoodsModel.query.filter(GoodsModel.name == n).first()
    # goods.name = 'fuck'
    # db.session.add(goods)
    # db.session.commit()
    
    # 更新方式二
    goods = GoodsModel.query.filter(GoodsModel.name == n).update({'name':'python'})
   
    return '更新货品'


# 商品删除
@api.route('/goods/delete/<int:id>')
def goods_delete(id):
    # 查询到指定货品
    goods = GoodsModel.query.filter(GoodsModel.id == id).first()
    print(goods)
    db.session.delete(goods)
    db.session.commit()
    return '删除货品成功'

# 客户


# 用户


# 物流


#
