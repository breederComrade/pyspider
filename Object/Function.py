# 函数

# 内置函数

# 函数定义

# 普通函数
# def Sum(x,y):
#     return x+y
# print(Sum(1,2))

# 匿名函数
# lambda 参数:返回值
# Sum = lambda x,y:x+y
# print(Sum(2,3))

# 闭包函数
''' def outer(a):
    b=10
    def inner():
        nonlocal b #表明这个b变量是上层控件变量
        b=20  # 如果nonlocal被设置了 那么b代表的是修改外部变量临时参数
        return a+b
    return inner
demo = outer(5)
print(demo()) '''

# 闭包函数在使用外部变量时只有一份变量
# def outer(a):
#     def inner(b):
#         nonlocal a
#         # 修改了临时变量 a只有一份 所以多次调用会把上次的值获得
#         # 条件是在同一个实例中调用
#         a = a+b
#         return a
#     return inner

# demo = outer(2)
# print(demo(3))
# print(demo(4))





# 函数传参

# 函数调用

# 函数

# 装饰器

# 带参数的装饰器
# def logger(func):
#     # 
#     @wraps(func) //这讲不会改变函数的__name__和属性
#     def wap(a):
#         va = func(a*2)
#         return va
#     return wap


# 被装饰的函数其实默认调用的是wap函数
# @logger
# def foo(a):
#     print('a:%s' % a)
#     return a*10

# print(foo(2))

# 类装饰器
''' class logging():
    def __init__(self, func):
        print('给函数添加装饰器时候使用')
        self.func = func

    def __call__(self, *args, **kwargs):
        print('函数被调用时候使用')
        print("[DEBUG]: enter function {func}()".format(func=self.func.__name__))
        print(args[1])
        print(kwargs['something'])
        return self.func(*args, **kwargs)
@logging
def say(d,f,something='some'):
    print("say {} {} {}!".format(d,f,something))
 '''
# 带参数的类装饰器
from functools import wraps
class logger(object):
    # 带参数的类装饰器
    # 
    def __init__(self, lev='info'):
        self.lev = lev
    def __call__(self,func):
        # 保持原函数的元信息
        @wraps(func)
        def wrapper(*args,**kwargs):
              print ("[{lev}]: enter function {func}()".format(
                lev=self.lev,
                func=func.__name__))
              func(*args,**kwargs)
        return wrapper      
              

@logger(lev='fuck')
def say(d,f,something='some'):
    print("say {} {} {}!".format(d,f,something))

say('f','d',something='fuck')


print(say.__name__)

# 内置装饰器
# @staticmethod : 类静态方法 实例和类都可执行
#    与成员方法的区别是没有self参数，并且可以在类不进行实例化的情况下调用
# @classmethod : 类方法
#    与成员方法的区别在于所接收的第一个参数不是self(类实例的指针)，而是cls (当前类的具体类型)
# @property : 属性方法
#   将一个类方法转变成一个类属性，只读属性
