#2-14 元组和多维容器
#元组(tuple)一旦被确定无法像列表重新赋值
#特性：有序；元素可重复；可以存放多种数据类型
#不支持元素修改(不支持增加，删减，赋值)
#元组用在对安全性有一定需求的数据上，即用在那些令所有人都无法更改的场景
# tuple=('张三','李四','王五','赵六')
# print(tuple[1])
# print(tuple[-3])
# print(tuple[1:3])#切片

#多维容器
# lista=[213,214,215,216,217,2182,219]
# listb=[1,2,3,4,5,'你好',(1,156,165,165,'广州',5,64,6,4),7,8,9]#多维容器（三维列表嵌元组）
# lastc=[25,561,561,651,51,65165,165]
# lastx=[lista,listb,lastc,[1561,45,46,154,796,1]]#二维的列表（列表中有列表）
# print(lastx[1][6][4])
