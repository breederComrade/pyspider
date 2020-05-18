# 字符串和数值
str1 = '自猝死'
str2 = 'fuck'
str3 = str1

# print(str1)
# 查询
# 格式ei
# 使用这种方法格式化字符串 0，1,2需要有秩序 不能0，2，3这种
# print("{0},{1},{2}".format('a', 'v', 'c'))
# print("{},{},{}".format('a', 'v', 'c'))
# print("{fuck},{fuck2}".format(fuck='fuck',fuck2='fuck2'))
# coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
# print('Coordinates: {latitude}, {longitude}'.format(**coord))
# print('fuck'[2:3])
# print('fuck'[:-2])
# print('fuck'[-1:])
# # 倒序 
# print('fuckfuck2'[::-1])
# # 倒序每2个取一次
# print('fuckfuck2'[::-2])
# print('fuckfuck2'[::2])
# # 大写
# print('fuckfuck2'.upper())
# # 小写
# print('FFFFFF'.lower())
# # 以什么结尾
# print('fuckfuck'.endswith('f',0,6))
# # 在方位内以什么开头
# print('fuckfuck'.startswith('f',))
# # 统计 f出现几次
# print('fuck'.count('f'))
# # 去除前后空格
# print('   fuck  '.strip())
# print('fukc f fuck '.strip('f'))
# s = "alexdsba"
# s1 = s.strip("a") # 可以指定内容去除 只去除头和尾
# print(s1)
# 首字母大写
# name = "alex"
# name1 = name.capitalize()
# print(name1)
# 每个单词首字母大写

# name = "jerry home"
# print(name.title())
# 大小写反转
# name = "JerryHome"
# print(name.swapcase())

# 填充居中---
# name = "jerry"
# print(name.center(30,"*"))

# 查找从左到右 只返回第一个
# name = "jerry"
# print(name.find("r"))
# 输出 2 (代表第一个"r"的下标）
      
# print(name.find("t"))
# 输出 -1 (find 查找不存在的返回 -1）
       
       
# print(name.index("t"))
# index 查找不存在的就报错

# 查找替换
#  find rfind lfind index rindex lindex replace
# print('fuck'.index('f'))
# print('fuck'.index('e')) :没有会报错
# print('fuck'.lfind('f'))

# 拼接
# print("_".join(name)) 
s = "zzzzxxx222"
# print(s.isalnum()) # 判断是不是字母,数字,中文
# print(s.isalpha())  # 判断是不是字母,中文
# print(s.isdigit())  # 判断字符串是不是全都是阿拉伯数字
# print(s.isdecimal())  # 判断是否是十进制

# 找出倒数第一个2
print(s.rfind("2",2,8))

# 切割
# str.split(s, num)[n]

