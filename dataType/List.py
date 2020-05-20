# 集合/数组
 
list = [1,2,3,'James','Paul']
list = [i for i in range(10)]
print(type(list))
# list.append() ：尾部新增元素
list.append('fuck')
print(list)
# list.insert()：插入元素  list.insert(index, object)  参数一：index 位置， 参数二：object
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')
print(fruits)
# list.extend()：扩展列表  list.extend(tablelist)，左右与 + 类似
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

# + 号用于组合列表， list1+list2
p = [1,2,2,2]
print(fruits+p)

# 重复列表
print(p*3)

# 循环
for index, item in enumerate(list):
    print(index+1, item)
# 删除
print(list)
# 如果不存在会报错 只会删除最靠前的
list.remove(2)
print(list)

# list.pop(index)： 默认为删除最后一个元素，index -- 可选参数，要移除列表元素的对应索引值，
# del list[index] ：可以删除整个列表或指定元素或者列表切片，list删除后无法访问。

# list.reverse() ：列表元素反转
#  a.sort(reverse=True)，降序排序 
# 　注：sorted()函数与sort()方法有一点不同，sort()会在原list的上重新排列并保存，而sorted()不会改变原列表的顺序，只是生成新的排序列表

L = ['spam', 'Spam',  'SPAM!', 'Sam', 'Paul','Kate']
''' 
　L[2]               'SPAM!'                     读取列表中第三个元素

　　L[-2]              'Paul'                         读取列表中倒数第二个元素

　　L[1:]              ['Spam',  'SPAM!', 'Sam', 'Paul','Kate']      从第二个元素开始截取列表

　　L[1:4:2]         ['Spam', 'Sam']          从第二个元素开始到底到第五个元素，每两个元素选取一个
 '''
 
 


# 　　len(list)：列表中元素个数

# 　　max(list)：返回列表元素最大值

# 　　min(list)：返回列表元素最小值

# 　　list(seq)：将元组转换为列表

# 　　tuple(seq)：将列表转换为元祖

# 　　sorted(list)：排序列表元素顺序
# list.clear()：  清空列表  (python3.0)