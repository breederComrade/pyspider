#
# 模块包
import os

class modulesFile:
    # 构造函数
    def __init__(self):
        self.name = 'fuck'
    # 成员方法
    def showName(self):
        self.name = os.path.realpath(__file__)
        print(self.name)
        return self.name
