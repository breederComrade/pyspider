from app.extension import ma

# class GoodsSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'name', 'code')
#         # mode = GoodsModel
#
#     # Smart hyperlinking
#     _links = ma.Hyperlinks(
#         {"self": ma.URLFor("goods", id="<id>"), "collection": ma.URLFor("goods")}
#     )
from app.models import GoodsModel


#
# class GoodsSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model = GoodsModel
#     id = ma.auto_field()
#     name = ma.auto_field()
#     code = ma.auto_field()

class GoodsSchema(ma.SQLAlchemyAutoSchema):
    # ？：隐藏个别数据
    class Meta:
        model = GoodsModel
    #     关键字 关系表字段
    # fuck = ma.HyperlinkRelated("flask_marshmallow")
    #  外键
    # books = ma.List(ma.HyperlinkRelated("flask_marshmallow"))


good_schema = GoodsSchema()
goods_schema = GoodsSchema(many=True)
