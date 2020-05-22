import random
from flask import Flask,Blueprint,render_template,request,redirect,jsonify
# from flasgger import Swagger,swag_from
# 创建flask项目
# from flask_restplus import Api
from flask_restx import Api, Resource, fields

app = Flask(__name__)

# debug模式
app.debug = True


# Flask -flasgger
# swagger_config = Swagger.DEFAULT_CONFIG
# swagger_config['title'] = '电商'    # 配置大标题
# swagger_config['description'] = '测试'    # 配置公共描述内容
# swagger_config['host'] = 'config.SWAGGER_HOST'    # 请求域名
#
# swagger_config['swagger_ui_bundle_js'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js'
# swagger_config['swagger_ui_standalone_preset_js'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js'
# swagger_config['jquery_js'] = '//unpkg.com/jquery@2.2.4/dist/jquery.min.js'
# swagger_config['swagger_ui_css'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui.css'
#
# Swagger(app, config=swagger_config)
#

# flask-restx 文档生成方法
# #
# api = Api(app,title='fuck')
#
#
#
# @api.route('/hello')
# class HelloWorld(Resource):
#          def get(self):
#              return {'hello': 'world'}
#
# @api.route('/<string:language>')
# class HelloWorld2(Resource,):
#     def get(self,language):
#         return {'hello': 'world'+language}
#     def post(self,language):
#         return {'hello': 'world'+language}





@app.route('/api/<string:language>/',methods=['GET'])
def index(Resource):
    """
            方法名称：通过ID查询用户
            方法描述：通过输入ID调用此API查询用户
            ---
            tags:
                - 接口名称:用户管理API
            parameters:
                - name: id
                  in: path
                  type: string
                  required: true
                  description: 需要查询的用户ID
            responses:
                500:
                    description: 状态描述：Error The language is not awesome!
                200:
                    description: 状态描述：返回成功json格式
                    schema:
                        id: Success
                        properties:
                            code:
                              type: string
                              description: 状态码
                              default: 200
                            msg:
                              type: string
                              description: 信息
                              default: 'OK'
                            error_code:
                              type: string
                              description: 错误码
                              default: 0
    """
    language = language.lower().strip()
    features = [
        "awesome", "great", "dynamic",
        "simple", "powerful", "amazing",
        "perfect", "beauty", "lovely"
    ]
    size = int(request.args.get('size', 1))
    if language in ['php', 'vb', 'visualbasic', 'actionscript']:
        return "An error occurred, invalid language for awesomeness", 500
    return jsonify(
        language=language,
        features=random.sample(features, size)
    )


# 配置路由goods
# @app.route('/')
# def hello_word():
#     return 'hello world!'


@app.route('/goods')
def goods(Resource):
    return 'goods'


# post
@app.route('/post', methods=["POST","GET"])
def postPage():
    return {
        "fuck": 'fff'
    }


# 请求方法
# @app.route('/get',methods = ("GET"))
# @app.route("/anything", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "TRACE"])

# 动态地址
# @app.route(
#     "/anything/<path:anything>",
#     methods=["GET", "POST", "PUT", "DELETE", "PATCH", "TRACE"],
# )

# @app.route("/stream/<int:n>")


# 返回数据json 序列化

# 302跳转

# cookies

# session


# token


# 报错

# 多个路由


# 子路由

#

# 蓝图配置

# @app_before_request
# 请求前


# @app.after_request
# 请求后

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8233)
