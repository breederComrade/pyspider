from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api.main import api
from app.config import Config,config_map
from app.extension import init_ext


def create_app(config_name):
    # app.app
    app = Flask(__name__)
    # 设置
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
   
    # 404处理
    @app.errorhandler(404)
    def page_not_found(e):
        return 'page_not_found-404'
    # 500处理
    @app.errorhandler(500)
    def server_no_respone(e):
        return '500,server_no_respone'
    # 蓝图
    register_blueprints(app)
    # 初始化
    init_ext(app)
    return app


#    注册蓝图
def register_blueprints(app):
    app.register_blueprint(api, url_prefix='/api')

#     注册扩展

#     错误绑定

#      命令
#      输出日志
