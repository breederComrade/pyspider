# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from app.models.address import Address

class AddressDao():
    # 更新「配送信息」
    @staticmethod
    def update_address(id, user_id, **form):
        address = Address.get_or_404(id=id, user_id=user_id)
        address.update(**form)
    
    # 删除「配送信息」
    @staticmethod
    def delete_address(id, user_id):
        address = Address.get_or_404(id=id, user_id=user_id)
        address.delete()

