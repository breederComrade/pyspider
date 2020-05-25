import random
from flask import Flask, Blueprint, render_template, request, redirect, jsonify
# from flasgger import Swagger,swag_from
# 创建flask项目
# from flask_restplus import Api
from flask_restx import Api, Resource, fields

app = Flask(__name__)

# debug模式
app.debug = True


# 首页
@app.route('/', methods=["Get"])
def Index():
    # 跳转
    return redirect('/home')
    # return '首页'


# 跳转301
# route上的跳转
@app.route('/home', redirect_to="/endpoint")
def home():
    return 'indexRest'


# 访问点 让url映射找到指定视图函数 自定义访问点 可用于分辨url
# 如两个蓝图都有active路由 这个时候flask无法分辨到底是哪个
@app.route('/endpoint', endpoint='changeEndpoint')
def endpoint():
    return ''


#  默认参数
@app.route('/default', defaults={'id': 22})
def deft(id):
    # r'Stirng' 去除转义字符 转义字符无用
    # f'Stirng'  支持{}包裹的python表达式
    # b'Stirng'  后面字符串为bytes类型
    # u'Stirng' 含有中文字符的
    return f'{id}'


# 动态url标签
#  query /xxxx/xx

@app.route('/query/<path:lang>')
def query(lang):
    return '动态路由:%s' % lang


#
# parmary /xxx?id=sss
# <name> <String:name><int:name><path:name> <float:name> 指定类型变量
# url规则是不能有/的 如：/parmary/fuck/fff.txt  变量部分是不能有/ 所以使用path
#
@app.route('/parmary/<path:name>')
def parmary(name):
    p = request.args.get('p')
    type = request.args.get('type')
    print(p)
    print(type)
    return jsonify({'t': [p, type], 'name': name})


# 访问点/endpoint


# 默认404


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
