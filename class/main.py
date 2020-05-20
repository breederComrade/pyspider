# 类型
# 
# 创建类
# class logger:
#     def __init__(self,*args,**kwargs):
#         print('fuck',args[0],kwargs)

# log = logger('fuck',fuck='fc')   

# 构造函数
class Fuck:
    name='xxx'
    def __init__(self,name):
        print('触发构造函数')
        # 构造函数
        self.name = name
        # 局部变量无法访问
        # name ='fuck'
    # 不可被类直接调用只可实例调用
    # 可以想Fuck.showName(a)传参来调用
    def showName(self):
        print(self.name)
        # return num;
    # 成员方法
    def method(self):
        print(self.name)
    
    # 类静态方法
    # 无法使用self
    # 可被类和类实例调用
    @staticmethod
    def showNameStatic():
        # 访问类静态变量
        # 
        print('showName',Fuck.name)
        
        # return num;
    # 类的方法
    # 类方法可以被实例和类调用
    # 但是类中属性不会被赋值
    @classmethod
    # 不适用self 使用cls上下文
    def classMethod(cls):
        print('类方法',cls.name)
    # 类属性

# fuck = Fuck('I a name')
# fuck.method()
# fuck.classMethod()
# Fuck.showName()    

# 继承
# python的继承是通过()来实现
class Extend(Fuck):
    age=3
    def __init__(self):
        # 调用父类的构造函数初始化父类属性
        # super().__init__('extend')
        # 调用父类构造汗 与上面暗中结果一夜但是有区别
        print(Fuck.__init__(self,'fuck') )
        self.age = 4
        print('子类构造函数')
    # 实例方法
    def extendShowName(self):
        # 访问类变量 非实例
        print(self.__class__.age)
        # 调用实例后属性
        print(self.age)
        # 调用父类方法
        # super第一参数传继承类 
        super(Extend,self).showName()
        # 调用父类的属性将保持初始化状态而不是构造函数赋值
        print(super(Extend,self).name)
    
# extend = Extend()
# extend.showName()
# extend.extendShowName()

# 多层继承




# 接口继承
# 继承父类并且实现接口中定义的方法 类似抽象类
import abc
class All_file(metaclass=abc.ABCMeta):  #继承抽象类基类
    name='fuck'
    
    def __init__(self,name):
       print('执行父类构造函数')
       self.name = name
    
    @abc.abstractmethod                  #加上abc.abstractmethod 代表子类需要实现 不实现子类无法实例化
    def read(self):
        pass
    @abc.abstractclassmethod
    def write(self):
        pass
class Txt(All_file):
    # 子类构造函数有的话 实例化传值必须存在
    # 如果子类构造函数没有操作父类构造函数会处理
    # 注意子类没有声明构造函数的时候 父类的构造函数会被调用
    # def __init__(self,name):
    #     pass
    def read(self):
        print('读取')
    def write(self):
        print('写入')

# 继承类构造函数传参子类没有满足的构造函数的话会被父类构造函数调用
txt = Txt('你妈比')
print('naame',txt.name)
txt.read()
print('子类属性字典',txt.__dict__)

# 混合

# 