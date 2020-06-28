# _*_ coding: utf-8 _*_
"""
  Created by wangjun on 2020/06/10.
  __author__ = 'wangjun'
"""
# _*_ coding: utf-8 _*_
from werkzeug.datastructures import Authorization

"""
  Created by Allen7D on 2018/6/13.
"""
from collections import namedtuple
from functools import wraps

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth as _HTTPBasicAuth,HTTPTokenAuth as _HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer \
    as Serializer, BadSignature, SignatureExpired

from app.models.user import User
from app.libs.error_code import AuthFailed
from app.core.auth import is_in_auth_scope

'''
    HTTTP授权验证流程
    1、通过HTTPTOENAUTH实例对象auth
    2.auth.login.reuired 定义蓝图调用时调用login_required方法
    3.在调用login_required装饰器是 首先会通过getauth获取用户token
    4.getAuth内部实现是通过通过self.header是否可以直接在request.authorization中获取
    5.如果获取不到 试着从headers['authorization']获取
    6.然后返回一个 Authorization(auth_type, {'token': token})类
    7.获取authl值后调用user = self.authenticate(auth, password)
    8.self.authenticate总通过获取的auth['token']来获取token具体值
    9.verify_token_callback在通过该函数定义的装饰器函数解析token是否有效
    10.g.flask_httpauth_user通过这个将数据存储起来
    ps:在每次调用需要登录接口都会调用这个流程 所以g是在当前调用有用的
    在当前数据中查找都是正确的
'''

# 继承HTTPtokenauth类
class HTTPTokenAuth(_HTTPTokenAuth):
    def __init__(self, scheme='Bearer', realm=None):
        super(HTTPTokenAuth, self).__init__(scheme, realm)
    
    # 验证管理员装饰器
    def admin_required(self, f):
        f.__doc__ = '👑' + f.__doc__
        @wraps(f)
        def decorated(*args, **kwargs):
            # 获取指定值
            auth = self.get_auth()
            if request.method != 'OPTIONS':
                [username, client_password] = [auth.username, auth.password] \
                    if auth else ['', '']
                if self.verify_admin_callback:
                    self.verify_admin_callback(username, client_password)
            return f(*args, **kwargs)
    
        return decorated
        
    # 设置验证管理员校验用户函数
    def verify_admin(self,f):
        self.verify_admin_callback = f
        return f
    
    # 设置验证权限组的方法
    def verify_group(self, f):
        self.verify_group_callback = f
        return f
    def get_auth(self):
        auth = None
        if self.header is None or self.header == 'Authorization':
            auth = request.authorization
            if auth is None and 'Authorization' in request.headers:
                # Flask/Werkzeug do not recognize any authentication types
                # other than Basic or Digest, so here we parse the header by
                # hand
                try:
                    print(request.headers['Authorization'].split(
                        None, 1))
                    auth_type, token = request.headers['Authorization'].split(
                        None, 1)
                    auth = Authorization(auth_type, {'token': token})
                except (ValueError, KeyError):
                    # The Authorization header is either empty or has no token
                    pass
        elif self.header in request.headers:
            # using a custom header, so the entire value of the header is
            # assumed to be a token
            auth = Authorization(self.scheme,
                                 {'token': request.headers[self.header]})
    
        # if the auth type does not match, we act as if there is no auth
        # this is better than failing directly, as it allows the callback
        # to handle special cases, like supporting multiple auth types
        if auth is not None and auth.type.lower() != self.scheme.lower():
            auth = None
    
        return auth
    # 在login_requiere装饰器调用会先调用这个auth = self.get_auth()
    # auth 是通过get_auth获得
    # 调用login_requiere装饰器 其中有user =  user = self.authenticate(auth, password)
    # 会调用这局用于获取后台验证
    def authenticate(self, auth, stored_password):
       
        if auth:
            token = auth['token']
        else:
            token = ""
        if self.verify_token_callback:
            return self.verify_token_callback(token)

class HTTPBasicAuth(_HTTPBasicAuth):
    def __init__(self, scheme=None, realm=None):
        super(HTTPBasicAuth, self).__init__(scheme, realm)
        self.hash_password(None)
        self.verify_password(None)
    
    def admin_required(self, f):
        f.__doc__ = '👑' + f.__doc__
        
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if request.method != 'OPTIONS':
                [username, client_password] = [auth.username, auth.password] \
                    if auth else ['', '']
                # 验证是否是管理员
                # 采用的是装饰器
                #
                if self.verify_admin_callback:
                    self.verify_admin_callback(username, client_password)
            return f(*args, **kwargs)
        
        return decorated
    # 是否是管理员
    def verify_admin(self, f):
        self.verify_admin_callback = f
        return f
    
    def group_required(self, f):
        f.__doc__ = '🔰' + f.__doc__
        
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if request.method != 'OPTIONS':
                [username, client_password] = [auth.username, auth.password] \
                    if auth else ['', '']
                if self.verify_group_callback:
                    self.verify_group_callback(username, client_password)
            return f(*args, **kwargs)
        
        return decorated
    
    def verify_group(self, f):
        self.verify_group_callback = f
        return f


# auth = HTTPBasicAuth(scheme='bearer')
auth = HTTPTokenAuth()
UserTuple = namedtuple('User', ['uid', 'ac_type', 'scope'])


##### 超级管理员的API校验 #####
@auth.verify_admin
def verify_admin(token, password):
    # 解析管理员
    (uid, ac_type, scope) = decrypt_token(token)
    # 数据库查找这个用户
    current_user = User.get_or_404(id=uid)
    # 如果用户不是管理员
    if not current_user.is_admin:
        # 报错
        raise AuthFailed(msg='该接口为超级管理员权限操作')
    # 否者定义到全局管理器
    g.user = current_user  # UserTuple(uid, ac_type, scope)

##### CMS授权的管理员的API校验 #####
@auth.verify_group
def verify_group(token, password):
    (uid, ac_type, scope) = decrypt_token(token)
    current_user = User.get_or_404(id=uid)
    group_id = current_user.group_id
    # 非admin用户，先进行校验
    if not current_user.is_admin:
        if group_id is None:
            raise AuthFailed(msg='您还不属于任何权限组，请联系系统管理员获得权限')
        allowed = is_in_auth_scope(group_id, request.endpoint)
        if not allowed:
            raise AuthFailed(msg='权限不够，请联系系统管理员获得权限')
    
    g.user = current_user  # UserTuple(uid, ac_type, scope)


##### 普通用户的API校验 #####
# @auth.verify_password
# def verify_password(token, password):
#     user_info = verify_auth_token(token)
#     if not user_info:
#         return False
#     g.user = User.get_or_404(id=user_info.uid)  # 用「g.user」来记录登录的状态；g只能用于一次请求
#     return True


# 验证token
# token是通过get_auth获得
# 调用这个函数用于解析token
# 如果解析正确就返回
# 如果解析错误就就返回false
# 返回false会报错
@auth.verify_token
def verify_token(token):
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    g.user = User.get_or_404(id = user_info.uid)
    return True

# 用于解析token
def verify_auth_token(token):
    # 经过token的解析(包含校验层)
    (uid, ac_type, scope) = decrypt_token(token)
    return UserTuple(uid, ac_type, scope)


def decrypt_token(token):
    '''
    解析(包含校验层)Token成 UserTuple(uid, ac_type, scope)
    :param token:
    :return:
    '''
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)  # token在请求头
    except BadSignature:
        raise AuthFailed(msg='token 无效', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token 过期', error_code=1003)
    uid = data['uid']  # 用户ID
    ac_type = data['type']  # 登录方式
    scope = data['scope']  # 权限
    return UserTuple(uid, ac_type, scope)


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    '''生成令牌'''
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    token = s.dumps({
        'uid': uid,
        'type': ac_type,
        'scope': scope
    })
    return {'token': token.decode('ascii')}
