# 红图
class Redprint:
    def __init__(self, name):
        self.name = name
        # 存储每个绑定的红图函数
        self.mond = []
    
    # 路由装饰器
    def route(self, url, **options):
        def decorate(f):
            self.mond.append((f, url, options))
            return f
        
        return decorate
    
    # 注册
    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = "/" + self.name
        for f, url, options in self.mond:
            endpoint = options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix, endpoint, f, **options)
