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
# @api.doc(args=['g.body.account','g.body.secret','g.body.type'],body_desc='''登录的基本信息: 账号、密码、登录类型:
#                                                            - 用户名登录(type:100)
#                                                            - 邮箱账号登录(type:101)
#                                                            - 手机账号登录(type:102)
#                                                            - 小程序登录(type:200)
#                                                            - 微信扫码登录(type:201)''')
def get_token():
    return Success()
