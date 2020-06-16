# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/11.
  author: wangjun
  description: 
  
"""


# Swagger相关配置
description = '''
👑标注的接口，只有超级管理员(admin)的权限才能访问；
🔰标注的接口，需要有相应权限组(group)的权限才能访问；
🔒标注的接口，需要登录(login)获取Token才能访问。

API接口分为cms版本和v1版本，大部分接口需要token权限才能访问。
访问之前，先使用/v1/token查询token，并将token放入Authorize中。
'''

'''
内部只支持http
外部（云服务器）支持 https 和 http 协议
'''
SWAGGER_TAGS = []  # 在'/app/__init__.py'的register_blueprint函数中设置
# swagger插件初始化时会读取app.config中的swagger配置
# 在这里可以设置swagger的配置 入tags 引用
SWAGGER = {
    'swagger_version': '2.0',
    'info': {
        'title': '华人社区 API',
        'version': '0.1.0', # 项目版本
        'description': description,
        # 'contact': {
        #     'responsibleOrganization': 'Shema(聆听)',
        #     'responsibleDeveloper': 'wangjun',
        #     'email': 'bodanli159951@163.com',
        #     'url': 'http://ivinetrue.com'
        # },
        # 'termsOfService': 'http://ivinetrue.com'
    },
    'host': '',
    'basePath': '/',  # base bash for blueprint registration
    'tags': SWAGGER_TAGS, # 接口在文档中的类别和顺序
    'schemes': ['http','https'], # 通信协议: http或https或多个，默认http
    'operationId': 'getmyData',
    # token
    'securityDefinitions': {
        'basicAuth': {
            'description': 'Authorization format: \n &nbsp; Username: &nbsp;{token} \n &nbsp; Password: &nbsp; {非空即可}',
            'type': 'basic'
        }
    },
    # "securityDefinitions": {
    #     "Bearer": {
    #         "name": "xxx",
    #         "in": "header",
    #         "type": "apiKey",
    #         "description": "Bearer JWT"
    #     }
    # },
    # "security": [
    #     {
    #         "Bearer2": []
    #     }
    # ],
}

