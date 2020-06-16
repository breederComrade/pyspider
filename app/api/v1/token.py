# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from app.core.error import Success
from app.extensions.api_docs.redprint import Redprint

api = Redprint(name='token', description='登录令牌')


@api.route('', methods=['POST'])
@api.doc()
def get_token():
    # token = Token.get
    return 'token'

@api.route('/verify', methods=['POST'])
@api.doc()
def verify():
    '''解析令牌'''
    return '解析令牌'

