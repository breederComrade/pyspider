# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/7/12
  author: wangjun
  description:  商品操作Dao
  
"""
from sqlalchemy import desc
from app.core.db import db
from app.models.product import Product


class ProductDao(object):
    def create_product(form):
        with db.auto_commit():
            Product.create(
                commit=False,
                name=getattr(form, 'name', None),
                price=getattr(form, 'price', 0),
                remark=getattr(form, 'price', ''),
                stock=getattr(form, 'stocknum', 0)
            )
    
    @staticmethod
    def update_product():
        pass
    
    @staticmethod
    def delete_product(id):
        # 获取id 是否存在
        # 需要登录
        product = Product.get_or_404(id=id)
        product.delete()
    
    # 获取最近上架的商品
    @staticmethod
    def get_most_recent(count):
        products = Product.query.order_by(desc(Product.create_time)) \
            .limit(count).all()
        return {
            'items': products
        }
    
    # 获取某商品详情
    @staticmethod
    def get_product(id):
        product = Product.get_or_404(id=id)
        return product.hide('category_id')
    
    # 查询某类别商品列表
    @staticmethod
    def get_list_by_category(c_id, page, size):
        '''
        :param c_id: 类别id
        :param page:
        :param size:
        :return:
        '''
        paginator = Product.query \
            .filter_by(category_id=c_id) \
            .paginate(page=page, per_page=size, error_out=False)
        return {
            'total': paginator.total,
            'current_page': paginator.page,
            'items': paginator.items
        }
