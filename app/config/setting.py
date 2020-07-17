# _*_ coding: utf-8 _*_
"""
  Created by wangjun on 2020/06/10.
  __author__ = 'wangjun'
"""

# _*_ coding: utf-8 _*_
"""
  Created by wangjun on 2020/06/10.
  __author__ = 'wangjun'
"""

from app.libs.enums import ClientTypeEnum

'''
应用于Swagger的URL，会自动添加协议前缀(http://或者https://)，因为会切换协议前缀
local_setting.py中 SERVER_URL = '127.0.0.1:8010'
'''
SERVER_URL = 'server.mini-shop.ivinetrue.com'  # 外部（云服务器）地址
# 所有红图的路径
API_PATH = 'app.api'
# all api by module(version)
# 可以控制Swagger API文档的显示顺序
# TODO:更具版本号来设置目录
ALL_RP_API_LIST = ['v1.test', 'v1.token', 'v1.user','v1.role','v1.auth', 'v1.group', 'v1.product','v1.spec', 'v1.order', 'v1.address', 'v1.company',
                   'v1.customer', 'v1.express_company', 'v1.express', 'v1.category', 'v1.pay']

# 所有endpoint的meta信息
EP_META = {}
EP_INFO_LIST = []
EP_INFOS = {}

# 分页配置
PAGE_DEFAULT = 1
SIZE_DEFAULT = 10

# 项目的github地址
GITHUB_URL = 'https://github.com/Allen7D/mini-shop-serve'
# 项目文档地址
DOC_URL = 'http://doc.mini-shop.ivinetrue.com'

# 登录类型(站内)
CLINET_INNER_TYPES = (ClientTypeEnum.USERNAME, ClientTypeEnum.EMAIL, ClientTypeEnum.MOBILE)
