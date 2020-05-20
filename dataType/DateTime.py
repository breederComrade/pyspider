# 日期时间

import datetime 



# 获取当前日期
# 
now = datetime.datetime.today()
print(now)
# 获取属性相等写法
print(now.__getattribute__('year'))
print(now.year)

# 获取年月日时分秒
print('%s年%s月%s日 %s时%s分%s秒' % (now.year,now.month,now.day,now.hour,now.minute,now.second))

# 转换成字符串
print(type(str(now))) #== now.__str__()

# 格式化时间
# 日期时间
# a= datetime.datetime(2017,3,15,2,3,4)
# 日期
a= datetime.date(2019,5,20)
print(a)

# 指定格式输出
print(a.__format__('%Y_///%m_///%d')) #===a.strftime("%Y%m%d")相同

# 相隔几天
b = datetime.date(2019,5,22)
print(b.__sub__(a))
print(a.__sub__(b))
c = a.__sub__(b)

# 