# 
class testClass:
    # 属性
    name = ''
    age = ''
    
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def deBugPrint(self):
        print('self.name:{}'.format(self.name))


obj = testClass('wang', 19)
obj.deBugPrint()
