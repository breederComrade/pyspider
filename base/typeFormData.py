# 类型转换
# int() 转换成整数
# long() 长整数
# float()
# complex(real,[,image]) 复数
# str(x) 字符串
# repr(x) 将对象转换成字符串
r = 'RUNOOB'
print(repr(r))
dict = {'runoob': 'runoob.com', 'google': 'google.com'};
print( repr(dict))
# eval(str) python字符串表达式:将字符串表达式执行
x = 7
print('执行表达式:%s' % eval('3 *x'))
# tuple(s) 元祖
temp_list = [1,2,3]
tp = tuple(temp_list)
print(type(tp))
print(isinstance(tp,list))


# class A :
#     pass
# class B(A):
#     pass
# # A类的实例是服是A类
# print(isinstance(A(),A))
# # A类实例的类型
# print(type(A()))
# # B类实例是不是A类:Ture :isinstance类与type不同的是认为子类也是父类
# print(isinstance(B(),A))
# # B类实例的类型:fals
# print(type(B())==A)


# list(s) 列表
# chr(x)整数转换成一个字符
# unichr(x) 整数转unicode字符
# ord(x) 返回值是对应的十进制整数

# hex(x)整数===》16进制
# oct(x)整数===》八进制 

