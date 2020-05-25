from flask import Flask, Blueprint, blueprints, render_template

from goods.main import goods
# from user.main import user
# 包中导入
from user import user
from client.main import client

app = Flask(__name__)


@app.route('/', methods=['get'])
def index():
    return '首页'


# 注册蓝图
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(goods, url_prefix='/goods')
app.register_blueprint(client, url_prefix='/client')

if __name__ == '__main__':
    app.run(
        port=8999,
        debug=True
    )
