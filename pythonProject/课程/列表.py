#2-12  列表list
#特性：有序；元素可以重复；可以存放多种的数据类型

#通过索引（下标）获取值
# lista=['张三','李四','王五','签到','jdwoin','nsajc','nasjxi']
#        0      1      2     3       4       5        6
#        -7    -6     -5     -4      -3      -2       -1
# print(lista)
# print(lista[2])

#切片(就像给黄瓜切片一样去截取列表的一部分)
# print(lista[1:3])

# print(lista[1:5:1])
# print(lista[1:5:2])#lista[1:5:2]---lista[起始索引：结束索引：步长（隔几个取）]

# print([lista[1:]])#获取某个索引之后的所有值
# print([lista[:6]])#获取某个索引之前的所有值（不包含该数）

#列表的修改
#列表的增加数据
# lista=['张三','李四','王五','签到','jdwoin','nsajc','nasjxi']
# lista.append('大宝')#在末尾添加元素
# lista.insert(2,'乔峰')#在指定位置添加一个元素
# print(lista)

#删除数据
# lista=['张三','李四','王五','签到','jdwoin','nsajc','nasjxi']
# lista.remove('王五')#直接删除一个具体元素
# lista.pop(2)#删除指定位置的元素
# print(lista)

#给元素重新赋值
# lista=['张三','李四','王五','签到','jdwoin','nsajc','nasjxi']
# lista[1]='张三丰'
# print(lista)