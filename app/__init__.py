import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from app.config import Config, config_map
from app.extension import init_ext
from flask.json import JSONEncoder as _JSONEncoder
from datetime import date
import json
# log配置
# from app.schemas import init_marshmallow
from app.views import api, goods, order, user, customer

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


def create_app(config_name):
    # app.app
    app = Flask(__name__)
    # 修改jsonEncoder方法
    app.json_encoder = JSONEncoder
    # 设置
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
    
    # 蓝图
    register_blueprints(app)
    # 扩展
    register_plugin(app)

    # 初始化
    init_ext(app)
    # init_marshmallow(app)
    
    return app


#    注册蓝图
def register_blueprints(app):
    goods.register(api, url_prefix='/goods')
    order.register(api, url_prefix='/order')
    user.register(api, url_prefix='/user')
    customer.register(api, url_prefix='/customer')
    
    app.register_blueprint(api, url_prefix='/api')


#     注册扩展
def register_plugin(app):
    apply_json_encoder(app)  # JSON序列化
    
    # pass
    # apply_json_encoder(app)  # JSON序列化
    # apply_cors(app)  # 应用跨域扩展，使项目支持请求跨域
    # connect_db(app)  # 连接数据库
    # 统一处理异常
    handler_error(app)
    #
    # # Debug模式(以下为非必选应用，且用户不可见)
    # apply_default_view(app)  # 应用默认路由
    # apply_orm_admin(app)  # 应用flask-admin, 可以进行简易的 ORM 管理
    # apply_swagger(app)  # 应用flassger, 可以查阅Swagger风格的 API文档
    # if app.config['DEBUG']:
    #     apply_request_log(app)  # 打印请求日志


#
def apply_json_encoder(app):
    app.json_encoder = JSONEncoder


#     错误绑定
def handler_error(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return 'page_not_found-404'

#      命令
#      输出日志
