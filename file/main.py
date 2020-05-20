# 文件操作
import os
import shutil

# 当前
# 当前文件路径
curpath = os.path.realpath(__file__)
# 当前文件目录
dir = os.path.dirname(curpath)
# 文件路径
file = dir +"/"+'test.txt'
# 是代表项目的目录
# listdir 工作目录下的所有目录名字 list格式

# print('工作目录',os.getcwd(),os.listdir())
# 删除多个目录：os.removedirs（r“c：\python”）
# 检验给出的路径是否是一个文件：os.path.isfile()
# 检验给出的路径是否是一个目录：os.path.isdir()
# 判断是否是绝对路径：os.path.isabs()
# 检验给出的路径是否真地存:os.path.exists()
# 
# 
# 返回一个路径的目录名和文件名:os.path.split() 
# print('os.path.split()',os.path.split())
# os.path.split('/home/swaroop/byte/code/poem.txt') 结果：('/home/swaroop/byte/code', 'poem.txt')
''' 
分离扩展名：os.path.splitext()

获取路径名：os.path.dirname()

获取文件名：os.path.basename()

运行shell命令:os.system() 

读取和设置环境变量:os.getenv() 与os.putenv()

给出当前平台使用的行终止符:os.linesep    Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'

指示你正在使用的平台：os.name 对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'

重命名：os.rename（old， new）

创建多级目录：os.makedirs（r“c：\python\test”）

创建单个目录：os.mkdir（“test”）

获取文件属性：os.stat（file）

修改文件权限与时间戳：os.chmod（file）

终止当前进程：os.exit（）

获取文件大小：os.path.getsize（filename）
'''
# 打开文件
# fo = open(file,'r')
# print ("文件名为: ", fo.name)

# 读取文件

# 读取所有内容 大文件不要用
# read = fo.read()
# print('整个文件：',read)
# 获取一行
# first_line = fo.readline()
# print('第一行:',first_line)
# 获取多行
# lines = fo.readlines()
# print('多行:',lines)
# 
# 
# 
# with open(file) as f:
#     print('内容运行完会自动关闭')

# 节省计算机内存资源
# with  open(file) as f:
#     for line in f.readlines():
#         print(f.readlines())
#         # index = f.readlines().index(line)
#         # print('%s行：'% index,line);


# fooo = open(file)
# # enumerate 将可遍历数据对象组合为一个索引序列，
# for index,line in enumerate(fooo):
#     print('{index}行:'.format(index=index),line)
    
# fooo.close()

# 模式
''' 
x， 只写模式【不可读；不存在则创建，存在则报错】
a， 追加模式【可读；   不存在则创建；存在则只追加内容】
"+" 表示可以同时读写某个文件

r+， 读写【可读，可写】
w+，写读【可读，可写】
x+ ，写读【可读，可写】
a+， 写读【可读，可写】

 '''
# 写入文件
fooo = open(file,'a',encoding="utf-8")
fooo.writelines(['fuck\n','xxxx\n'])
fooo.close()
  




# 修改文件


# 查询文件


# 添加数据

# 删除数据






# 关闭文件
# fo.close()



# 新增文件
# 新增目录 已存在报错
# os.mkdir(dir+'/fuck',)

# os.mknod(dir+'/fuck.txt')



# 移动
# shutil.move("oldpos","newpos")   

# 删除文件
# os.remove()

