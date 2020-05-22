from flask import Flask

# 创建flask项目
app = Flask(__name__)


# 配置路由goods
@app.route('/')
def hello_word():
    return 'hello world!'


@app.route('/goods')
def goods():
    return 'goods'


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8233)