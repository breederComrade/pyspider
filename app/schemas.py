# marshmallow 序列化
from flask_marshmallow import Schema, fields, Marshmallow

from app.extension import ma
from app.models import GoodsModel


# 货品表
class GoodsScheme(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GoodsModel
        # fields = ("id","name","code")
        
   

# 订单表

# 订单货品表

# 客户表

# 用户表
