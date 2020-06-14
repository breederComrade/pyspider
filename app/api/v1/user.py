# _*_ coding: utf-8 _*_
"""
  created by wangjun on 2020/06/10.
  author: wangjun
  project:有单生意
  description:  用户接口
  
"""
#
from flask import g

from app.core.error import Success
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import user as api_doc
from app.models.user import User

api = Redprint(name='user', description='用户', )


#
@api.route('', methods=['GET'])
def get_user():
    # get是我们自定义的方法本意是调用了fliterby
    user = User.get(id=g.user.id)
    return Success(user)

#
@api.route('/test', )
@api.doc(auth=True)
def test_user():
    return '测试用户'

# post


# get

# body