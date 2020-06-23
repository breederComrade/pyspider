# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from app.core.error import Success
from app.extensions.api_docs.redprint import Redprint
from app.service.login_verify import LoginVerifyService
from app.validators.forms import ClientValidator, TokenValidator

api = Redprint(name='token', description='登录令牌')


@api.route('', methods=['POST'])
@api.doc(args=['g.body.account','g.body.secret','g.body.type'],body_desc='''登录的基本信息: 账号、密码、登录类型:
                                                           - 用户名登录(type:100)
                                                           - 邮箱账号登录(type:101)
                                                           - 手机账号登录(type:102)
                                                           - 小程序登录(type:200)
                                                           - 微信扫码登录(type:201)''')
def get_token():
    '''获取token'''
    form = ClientValidator().nt_data
    token = LoginVerifyService.get_token(
        account = form.account,secret = form.secret,type = form.type
    )
    return Success(token)



@api.route('/verify', methods=['POST'])
@api.doc(args=['g.body.token'])
def verify():
    '''解析令牌'''
    # 验证表单
    token = TokenValidator().nt_data.token
    # 解析
    token_info = LoginVerifyService.decrypt_token(token)
    return Success(data=token_info)
