#2-15 字典(dict)用于告诉查找的地方
#dict={键：值}
#特性：无序；键值对形式；键不可以重复；一般使用字符串作为键；字典是没有索引的，利用键做索引
# dicta={'name':'张三','age':'18','hobby':'badminton'}
# #用键来获取值
# print(dicta["hobby"])

#修改字典的值
# dicta={'name':'张三','age':'18','hobby':'badminton'}
# dicta["hobby"]='play'
# print(dicta['hobby'])

#字典增加数据
# dicta={'name':'张三','age':'18','hobby':'badminton'}
# dicta['sex']='男'
# print(dicta)

#字典的删除数据
# dicta={'name':'张三','age':'18','hobby':'badminton'}
# dicta.pop('hobby')
# print(dicta)

#判断一个键是否存在
# dicta={'name':'张三','age':'18','hobby':'badminton'}
# print('sex'in dicta)
# print('hobby'in dicta)