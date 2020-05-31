# 模型
from datetime import datetime

from app.extension import db


class BaseModel(db.Model):
    __abstract__ = True
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class GoodsModel(BaseModel):
    __tablename = 'goods_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), unique=True, )
    no = db.Column(db.String(45), unique=True)
    num = db.Column(db.Integer, default=12, nullable=True)
    image = db.Column(db.String(256), unique=True)  # 商品图片 文件名唯一
    # good_tag = db.Column(db.String(128), db.ForeignKey('tag.name'))  # 商品所属分类
    price = db.Column(db.FLOAT(16))  # 现价
    old_price = db.Column(db.FLOAT(16))  # 原价
    start = db.Column(db.Integer)  # 星级>>>1-5星
    discount = db.Column(db.FLOAT(32))  # 折扣
    skull_num = db.Column(db.Integer, default=0)  # 库存
    sales = db.Column(db.Integer, default=0)  # 销量
    goods_info = db.Column(db.Text)  # 商品介绍
    share_link = db.Column(db.String(256))  # 分享链接
    state = db.Column(db.Integer, default=1)  # 商品是否上架 0表示未上架 1表示已经上架 默认直接上架商品
    # 外键关联第二步
    
    def __repr__(self):
        return '<货品 %r>' % self.name


# 货品分类
class GoodsCategoryModel(BaseModel):
    __tablename__ = 'goods_category_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), unique=True, nullable=False)
    parent = db.Column(db.Integer, default=0, )


# 规格
class SkuModel(BaseModel):
    __tablename__ = 'sku_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


# 图片地址
# class ImgModel()


# 订单表
class OrderModel(BaseModel):
    __tablename__ = 'order_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    remark = db.Column(db.String(512))  # 添加订单备注
    # user = db.Column(db.Integer, db.ForeignKey('user.id'))  # 绑定外键 对应哪个用户的订单
    user_detail = db.relationship("Detail", backref='orders')  # 该订单对应的商品 外键关联
    times = db.Column(db.BIGINT)
    pay = db.Column(db.Integer, default=0)  # 是否支付成功 0=待支付 1=支付成功
    cancel = db.Column(db.Integer, default=0)  # 订单是否取消 0=未取消 1=已经取消的订单
    alipay = db.Column(db.String(256))  # 支付宝支付后的订单号 用来验证是否收款
    pay_remark = db.Column(db.String(1024))  # 用户提交支付状态的时候的备注信息

    
# 订单货品详情
class OrderGoodsModel(BaseModel):
    __tablename__ = 'order_goods_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'))  # 该订单对应的商品id
    price = db.Column(db.String(32))  # 该订单对应金额
    num = db.Column(db.Integer)  # 购买该商品的数量
    
    # orderId = db.Column(db.Integer, db.ForeignKey('orders.order_id'))  # 该订单的id
    # user = db.Column(db.Integer, db.ForeignKey('user.id'))  # 哪个用户购买了该商品


# 客户表
class CustomerModel(BaseModel):
    __tablename__ = 'customer_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), )


# 地址表
class AddressModel(BaseModel):
    __tablename__ = 'address_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String(500))
    province = db.Column(db.String(45), )
    country = db.Column(db.String(45), default='中国')
    zip = db.Column(db.String(20), )
    city = db.Column(db.String(512))  # 城市
    area = db.Column(db.String(512))  # 地区
    address = db.Column(db.String(512))  # 街道等详细位置
    phone = db.Column(db.String(20))  # 收货电话
    name = db.Column(db.String(128))  # 收货人姓名
    remarks = db.Column(db.String(512)) # 备注
    default_add = db.Column(db.Integer, default=1)  # 是否为默认地址 1表示默认地址 0表示非默认地址
    # 外键第二步
    # users_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# 用户表
class UserModel(BaseModel):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, index=True)
    password = db.Column(db.String(45), nullable=False)
    mobile = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(64), unique=True, index=True)  # 邮箱
    birthday = db.Column(db.DATE)  # 出生日期
    sex = db.Column(db.String(32))  # 性别
    password_hash = db.Column(db.String(128), unique=True)  # 密码 哈希
    avatar_hash = db.Column(db.String(32))
    image = db.Column(db.TEXT)  # 图像
    account_atatus = db.Column(db.String(4))  # 账号状态
    activate = db.Column(db.String(4), default="1")  # 1表示未激活 2表示已经激活
    ac_type = db.Column(db.String(4), default="1")  # 1表示普通用户 2表示管理员后台账号
    info = db.Column(db.Text)  # 个性简介
    member_grade = db.Column(db.String(4), default="0")  # 会员等级
    account_point = db.Column(db.Integer, default=0)  # 会员积分
    uuid = db.Column(db.String(1024))
    # （设置外键的第二步）
    # users_id = db.relationship('Address')  # 会员收货地址外键关系关联
    # user_order = db.relationship('Orders')  # 订单信息外键关系关联
    # comment_user = db.relationship('Comment', backref='user')  # 会员评论信息外键关系关联
    # user_logs = db.relationship('UserLog', backref='user')  # 会员登陆日志信息外键关系关联
    # user_message = db.relationship('Message', backref='user')  # 会员登陆日志信息外键关系关联
    # user_car = db.relationship('BuyCar')  # 购物车外键关系关联
    # detail_user = db.relationship('Detail')  # 订单商品购买人 外键关系关联
    # col_user = db.relationship('Collect', backref='user')  # 收藏商品对应用户
    
    # address = db.relationship('AddressModel',backref = 'UserModel')
    
    def __repr__(self):
        return '用户:%r' % self.name


# 物流公司表
class ExpressModel(BaseModel):
    __tablename__ = 'express_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
