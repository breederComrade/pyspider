# 配置文件

class Config(object):
    # 数据库
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wangjun2013@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICHATIONS = True
    SQLALCHEMY_ECHO = True

    # redis配置
    # flask-session配置


class DevelopmentConfig(Config):
    # 开发环境
    DEBUG = True


class ProductionConfig(Config):
    # 生产环境
    DEBUG = False


config_map = {
    'develop': DevelopmentConfig,
    'production': ProductionConfig,
}
