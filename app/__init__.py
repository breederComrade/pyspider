import logging
import os
from http.client import HTTPException
from logging.handlers import RotatingFileHandler

from flask import Flask as _Flask, request, _request_ctx_stack, g
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from app.core.db import db
from app.core.error import APIException, ServerError
from flask.json import JSONEncoder as _JSONEncoder
from datetime import date, time
import json
# log配置
# from app.schemas import init_marshmallow

logging.basicConfig(level=logging.DEBUG)
file_log_handler = RotatingFileHandler('logs/log', maxBytes=1024 * 1024 * 100, backupCount=10)
formatter = logging.Formatter('%(levelname)s %(filename)s :%(lineno)d %(message)s')
file_log_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_log_handler)


#
# 定义jsonNcoder
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if (hasattr(o, 'keys') and hasattr(o, '__getitem__')):
            # 有keys和getitem证明是model
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default((self, 0))


class Flask(_Flask):  # 定义自己的Flask核心对象，继承原来的Flask核心对象
    # json_encoder = JSONEncoder # 替换原本的JSONEncoder
    pass


def create_app(config_name):
    # app.app
    app = Flask(__name__)
    # 加载配置文件
    load_config(app)
    # 注册蓝图
    register_blueprint(app)
    # 注册插件
    register_plugin(app)
    return app


#
def load_config(app):
    # 本地开发模式
    # from_object 会判断是否是字符串对象 如果是就用import_string导入模块
    if os.environ.get('ENV_MODE') == 'dev:local':
        app.config.from_object('app.config.local_secure')
        app.config.from_object('app.config.local_setting')
    else:
        app.config.from_object('app.config.secure')
        app.config.from_object('app.config.setting')
    #
    app.config.from_object('app.extensions.file.config')


#    注册蓝图
def register_blueprint(app):
   pass
   


def register_plugin(app):
    apply_json_encoder(app)  # JSON序列化
    
    # apply_cors(app)  # 应用跨域扩展，使项目支持请求跨域
    # TODO:xxxxxx
    connect_db(app)  # 连接数据库
    handle_error(app)  # 统一处理异常
    
    # Debug模式(以下为非必选应用，且用户不可见)
    apply_default_view(app)  # 应用默认路由
    apply_orm_admin(app)  # 应用flask-admin, 可以进行简易的 ORM 管理
    
    # TODO:xxxxxx
    apply_swagger(app)  # 应用flassger, 可以查阅Swagger风格的 API文档
    
    if app.config['DEBUG']:
        apply_request_log(app)  # 打印请求日志


# 替换flask原序列化
def apply_json_encoder(app):
    from app.core.json_encoder import JSONEncoder
    app.json_encoder = JSONEncoder


# 连接数据库
def connect_db(app):
    db.init_app(app)
    #  初始化使用
    # TODO：app_context使用方法
    with app.app_context():  # 手动将app推入栈
        db.create_all()  # 首次模型映射(ORM ==> SQL),若无则建表


# 绑定错误
def handle_error(app):
    @app.errorhandler(Exception)
    def framework_error(e):
        if isinstance(e, APIException):
            return e
        elif isinstance(e, HTTPException):
            return APIException(code=e.code, error_code=1007, msg=e.description)
        else:
            if not app.config['DEBUG']:
                return ServerError()  # 未知错误(统一为服务端异常)
            else:
                raise e

# 默认路由
def apply_default_view(app):
    pass

# admin
def apply_orm_admin(app):
    pass

# swagger
def apply_swagger(app):
    pass

# 打印日志

def apply_request_log(app):
    @app.before_request
    def request_cost_time():
        g.request_start_time = time.time()
        g.request_time = lambda: "%.5f" % (time.time() - g.request_start_time)
    
    @app.after_request
    def log_response(res):
        message = '[%s] -> [%s] from:%s costs:%.3f ms' % (
            request.method,
            request.path,
            request.remote_addr,
            float(g.request_time()) * 1000
        )
        req_body = request.get_json() if request.get_json() else {}
        data = {
            'path': _request_ctx_stack.top.request.view_args,
            'query': request.args,
            'body': req_body
        }
        message += '\n\"data\": ' + json.dumps(data, indent=4, ensure_ascii=False)
        # 设置颜色开始(至多3类参数，以m结束)：\033[显示方式;前景色;背景色m
        print('\033[0;34m')
        if request.method in ('GET', 'POST', 'PUT', 'DELETE'):
            print(message)
        print('\033[0m')  # 终端颜色恢复
        return res
