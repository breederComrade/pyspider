# api接口
import json

import random

from flask import Flask, Blueprint, request, current_app

from app.extension import db
from app.models import GoodsModel, UserModel, AddressModel, CustomerModel, ExpressModel, OrderGoodsModel, OrderModel, \
    Student, Teacher

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
    # TODO: 自动获取code
    # ? : 如何在新增的情况下拿到货品列表最大id 作为code的定位值
    # ？: 判断表中已经存在？
    # ？:
    #
    #
    goods = GoodsModel(name='货品%d' % random.randint(1, 1000), num=12, code="20200504%d" % random.randint(1, 1000),
                       price=500,
                       old_price=500, sales=45, skull_num=10, start=5, )
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
    goods = GoodsModel.query.filter(GoodsModel.name == n).update({'name': 'python'})
    
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


# 订单
# 列表
@api.route('/order')
def order_list():
    return '订单列表'


@api.route('/order/<int:id>')
def order_get(id):
    return '订单详情'


@api.route('/order/create')
def order_create():
    return '订单增加'


@api.route('/order/update/<int:id>')
def order_update(id):
    return '用订单修改'


@api.route('/order/delete/<int:id>')
def order_delete(id):
    return '删除订单'


# 客户
@api.route('/customer')
def customer_list():
    return '用户列表'


@api.route('/customer/<int:id>')
def customer_get(id):
    return '用户详情'


@api.route('/customer/create')
def customer_create():
    return '用户增加'


@api.route('/customer/update/<int:id>')
def customer_update(id):
    return '用户修改'


@api.route('/customer/delete/<int:id>')
def customer_delete(id):
    return '删除用户'


# 用户
# 列表
@api.route('/user')
def user_list():
    # 正向查询：一查多
    user = UserModel.query.get(34)
    print('user.address',user.address.first().address)
    return '用户列表'


@api.route('/user/<int:id>')
def user_get(id):
    return '用户详情'


@api.route('/user/create')
def user_create():
    address = AddressModel.query.get(52)
    print(address)
    str_start = random.choice(['135', '136', '138', '199', '182'])
    str_end = ''.join(random.sample('0123456789', 7))
    str_phone = str_start + str_end
    user = UserModel(mobile=str_phone, password=123,
                     username='用户{}'.format(random.randint(1, 1000), address=[address]),
                     sex=random.random())
    db.session.add(user)
    db.session.commit()
    return '用户增加'


@api.route('/user/update/<int:id>')
def user_update(id):
    user = UserModel.query.get(id)
    address = AddressModel.query.get(52)
    user.address = [address]
    
    db.session.add(user)
    db.session.commit()
    return '用户修改'


@api.route('/user/delete/<int:id>')
def user_delete(id):
    return '删除用户'


# 地址

# 列表
@api.route('/address')
def address_list():
    # 查询
    address = AddressModel.query.get(41)
    print('xxx',address.name)
    # 反向查询（多查一）
    print('user:',address.user_table.username)
    return '地址列表'


@api.route('/address/<int:id>')
def address_get(id):
    return '地址详情'


@api.route('/address/create')
def address_create():
    addresss =  AddressModel(
        city="上海",
        province='上海',
        country='中国',
        street='普陀区',
        zip='3330006',
        address='地址地址地址:{}'.format(random.randint(1,1000)),
        # users_id=32
    )
    db.session.add(addresss)
    db.session.commit()
    
    return '地址增加'


@api.route('/address/update/<int:id>')
def address_update(id):
    return '地址修改'


@api.route('/address/delete/<int:id>')
def address_delete(id):
    return '删除地址'
