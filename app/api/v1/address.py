# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from app.core.error import Success
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import address as api_doc
from app.models.address import Address

api = Redprint(name='address',description='配送地址',api_doc = api_doc)

@api.route('/all', methods=['GET'])
# @api.doc(auth=True)
def get_all_address():
    return  'xxx'
    '''查询所有「配送信息」'''
    address_list = Address.query.filter_by(user_id=g.user.id).all_by_wrap()
    return Success(address_list)
