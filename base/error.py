# 异常处理

# try--case
# try:
#     pass
# except Exception as identifier:
#     pass
# else:
#     pass

# 常用异常

# io异常 ioError
# try:
#     # f = open("file-not-exists", "r")
#     print('xx')
# except IOError as e:
#     print("open exception: %s: %s" %(e.errno, e.strerror))
# else:
#     print('else')
# finally:
#     print('xxx')

# 通过模块可报错位置和文件
# import traceback

# try:
#     1/0
# except Exception as e:
#     traceback.print_exc()

# 多个异常
# try:
#     a = {'a': 1, 'b': 2, 'c': 3}
#     print(a['d'])
# except (KeyError,AttributeError,IndexError) as e:
#     print('错误信息提示：%s'%e)

# 自定义异常
# try:
#     # raise ValueError('之错误')
#     raise Exception("tongyongcuowu ")

# except ValueError as e:
#     print(e)

# except Exception as e:
#     print(e)