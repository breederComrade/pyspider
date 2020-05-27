from app import db


# 商品数据模型
class Goods(db.Model):
    __tablename__ = 'goods_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)
    num = db.column(db.Integer, unique=True)
    def __repr__(self):
        return '货品名:%s' % self.name

