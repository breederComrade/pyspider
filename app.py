
from flask import Flask, Blueprint, blueprints, render_template, jsonify
# s数据库抽象类y
from flask_sqlalchemy import SQLAlchemy
from db.db_config import db_config
from goods.main import goods
# 包中导入
from user.main import user
from client.main import client

app = Flask(__name__)

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = db_config['DATABASE_URI']
# 提示
app.config['SQLALCHEMY_TRACK_MODIFICHATIONS'] = True
# 查看映射的sql语句
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

#
 # 用户数据模型
class User_Model(db.Model):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(20), unique=True)
    account = db.Column(db.String(45), unique=True)
    password = db.Column(db.String(45), unique=True)
    age = db.Column(db.Integer, default=18)
   
    # 如果写init  那就要指定赋值
    # 否则会自动对应值
    # def __init__(self, nickname,account,password,age):
    #     self.nickname = nickname
    #     self.password = password
    #     self.account = account
    #     self.age = age
        
        
@app.route('/user/list2', methods=['get'])
def indexlist():
    user = User_Model.query.first()
    # subAdmin = User_Model(nickname='subAdmin3',account='subAdmin3',password='123')
    # db.session.add(subAdmin)
    # db.session.commit()
    # print(user.nickname,user.id,user.password)
    return 'user'


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
