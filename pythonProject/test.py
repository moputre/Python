# 快捷注释ctrl+？

# name='张三'
# age=28
# hobby='打羽毛球'
# print('个人信息是：',name,age,hobby)


# 字符串
# a1='张三'
# b1='李四'
# c='666'
# print(a1+b1+c)


# 拼接函数用法 函数：format
# s1='come on!{}{}{}'.format('张三','李四','666')
# print(s1)


# print(a1+b1)#先整体后出现，有拼接
# print(a1,b1)#分别打印多个内容，没有拼接


# 转义字符
# 字符串一些表达特殊意义的字符
# x1='这是第一行，\n这是第二行'#\n换行符
# x2='我想上大学 \t真的很想上'#\t制表符大约是4个字符


# 取消字符 文件路径 网址
# s="C:\ProgramData\HP\HP Support Framework\Resources\tPSFMessenger"
# s2=r'C:\ProgramData\HP\HP Support Framework\Resources\tPSFMessenger'
# s3='C:\\ProgramData\\HP\\HP Support Framework\\Resources\\tPSFMessenger' #双重转义=不转义
# print(s)


# 2-7
# int（）将字符串中的数字改为整数
# s1='565'
# ns1=int(s1)
# print(ns1+66）
#
# float（）将其他类型转化为浮点型即小数
# s1='3.14'
# ns1=float(s1)
# print(ns1+0.2)
#
# 整数转成小数
# f1=34
# nf1=float(f1)
# print(nf1)
#
# 小数转成整数
# f1=3.14
# nf1=int(f1)
# print(nf1)
#
# str（）将其他类型转成字符串
# a=5
# b=9
# c=str(a)
# d=str(b)
# print(c+d)
#
# bool（）将其他类型转为布尔非正即误
# 表示空意义的数据将被转成false，其他数据都会转成true
# a=15
# b='hallo'
# print(bool(a))


# 2-8 接收键盘收入  函数input（）
# 数据的变量=input('提示语句')  提示语句只能是一个单独的字符串 不能有逗号及其他类型
# input输入的语句将会统一被解析为字符串 只需要进行转换就ok了【int float】
# money=input("请输入你的银行存款:")
# print('您的银行存款：',money)


# 2-10 运算符
# python中的主要运算符：算术运算符 赋值运算符 关系运算符 逻辑运算符
# 算术运算符：用于计算如：加减乘除
# a=5
# b=2
# print(a/b)#可以保留小数
# print(a//b)#只可以保留整数
# print(a%b)#获取余数
# print(a**b)#获取幂次方

# 赋值运算符：给变量赋值如：等号
# a=125
# b=a+1
# b+=126
# a+=5#在a的基础上再加5   a+=a+5
# print(a)
# print(b)

# 关系运算符：比较两个变量之间的关系
# >  <  ==  <= >=  !=(不等号)
# 关系运算符运算的结果一定是布尔值
# 等等== 不等！= 常用来判断字符串是否相等
# a=5
# b=126
# print(a!=b)
# c='hallo'
# d='hallo'
# print(c!=d)

# 逻辑运算符：判断表达式之间的逻辑关系
# and(两边都是正确的才是true) or（两边只要有一边满足则就是true） not（对右边的布尔值的表达式取反）
# print(5>3 and 6<3)#and左右两边都是布尔值
# print(5>3 or 6<3)#or左右两边都是布尔值
# print(not 55<3)#not只有右边才有布尔值


# 2-12  列表list
# 特性：有序；元素可以重复；可以存放多种的数据类型

# 通过索引（下标）获取值
# lista=['张三','李四','王五','签到','woodwind','msvc','nasalise']
#        0      1      2     3       4       5        6
#        -7    -6     -5     -4      -3      -2       -1
# print(lista)
# print(lista[2])

# 切片(就像给黄瓜切片一样去截取列表的一部分)
# print(lista[1:3])

# print(lista[1:5:1])
# print(lista[1:5:2])#lista[1:5:2]---lista[起始索引：结束索引：步长（隔几个取）]

# print([lista[1:]])#获取某个索引之后的所有值
# print([lista[:6]])#获取某个索引之前的所有值（不包含该数）

# 列表的修改
# 列表的增加数据
# lista=['张三','李四','王五','签到','woodwind','
# msvc','nasalise']
# lista.append('大宝')#在末尾添加元素
# lista.insert(2,'乔峰')#在指定位置添加一个元素
# print(lista)

# 删除数据
# lista=['张三','李四','王五','签到','woodwind','msvc','nasalise']
# lista.remove('王五')#直接删除一个具体元素
# lista.pop(2)#删除指定位置的元素
# print(lista)

# 给元素重新赋值
# lista=['张三','李四','王五','签到','woodwind','msvc','nasalise']
# lista[1]='张三丰'
# print(lista)


# 2-14 元组和多维容器
# 元组(tuple)一旦被确定无法像列表重新赋值
# 特性：有序；元素可重复；可以存放多种数据类型
# 不支持元素修改(不支持增加，删减，赋值)
# 元组用在对安全性有一定需求的数据上，即用在那些令所有人都无法更改的场景
# tuple=('张三','李四','王五','赵六')
# print(tuple[1])
# print(tuple[-3])
# print(tuple[1:3])#切片

# 多维容器
# lista=[213,214,215,216,217,2182,219]
# list=[1,2,3,4,5,'你好',(1,156,165,165,'广州',5,64,6,4),7,8,9]#多维容器（三维列表嵌元组）
# last=[25,561,561,651,51,65165,165]
# lastx=[lista,listb,lastc,[1561,45,46,154,796,1]]#二维的列表（列表中有列表）
# print(lastx[1][6][4])


# 2-15 字典(dict)用于告诉查找的地方
# dict={键：值}
# 特性：无序；键值对形式；键不可以重复；一般使用字符串作为键；字典是没有索引的，利用键做索引
# dicta={'name':'张三','age':'18','hobby':'badminton'}
# #用键来获取值
# print(dicta["hobby"])

# 修改字典的值
# dicta={'name':'张三','age':'18','hobby':'badminton'}
# dicta["hobby"]='play'
# print(dicta['hobby'])

# 字典增加数据
# dicta={'name':'张三','age':'18','hobby':'badminton'}
# dicta['sex']='男'
# print(dicta)

# 字典的删除数据
# dicta={'name':'张三','age':'18','hobby':'badminton'}
# dicta.pop('hobby')
# print(dicta)

# 判断一个键是否存在
# dicta={'name':'张三','age':'18','hobby':'badminton'}
# print('sex’in dicta)
# print('hobby'in dicta)


# 2-16 集合（set）无序不重复
# 用处：去除重复值，进行数学集合运算
# 特性：无序；元素不重复（有重复的元素只会打印出一个元素）；集合本质上是只有键的字典
# seta={1,35,153,13,165,1561,1,651,547,"hallo"}
# print(seta)

# 去重
# lista=[1,1,2,51,316551,165,1,0,1,651,20]
# seta={1,35,153,13,165,1561,1,651,547,"hallo"}
# n=set(lista)#set是将其他序列转换为set
# listb=list(seta)#将其他序列抓换为list
# print(n)
# print(listb)

# 集合运算
# seta={1,15,15,154,13,6,59,594}
# setb={854,489,4624,1,14,612,591,5,15}
# print(seta&setb)#获取交集
# print(seta|setb)#获取并集
# print(seta-setb)#获取差集（在seta中有但在setb中没有的）


# 2-17 len（）函数 获取序列长度（length）
# lista=[1,1321,5,1,15631,165,1,51,54,1531,31,313,1]
# seta={1,6511,651,31,531,34,8,9,97,87,54,59,4864,684}
# dicta={'name':'张三','age':'18','hobby':'play'}
# tuplea=(1,68,46,16,48,4453,74,61,2,626,51,8468)
# s1='hallo word!'#字符串实质是只保存字符的列表
# # n=len(lista)
# # print(n)
# print(len(lista))
# print(len(dicta))
# print(len(seta))#重复的元素是不会算到长度里面的
# print(len(s1))
# print(s1[2])#字符串也可以取值


# 第三章情景设置（3-1 3-2 3-3）
# 大宝想要买车，于是他做了以下计划
# 1.如果年底存款大于100万，买宝马！
# 2.如果年底存款大于50万，买丰田！
# 3.如果年底存款大于20万，买二手车！
# 4.否则，手里的自行车再修修！


# 3-1 控制结构概述
# 控制结构表示控制程序运行的顺序和结构
# 分为顺序结构 选择结构 循环结构
# 顺序结构：代码逐行执行且执行一遍
# 选择结构（分支结构，判断结构）：通过条件的判断来决定那些代码执行那些代码不执行
# 循环结构：代码的重复执行


# 3-2 if-else语句
# 适用于：单个条件判断
# 基本语法：
# if 判断语句
#     执行语句
# 只有当判断语句为真（True）的时候才执行冒号后下面的语句
# money=0
# if money>=100: #如果
# 	print('恭喜你可以买宝马了！')
# 	print('真开心')
# else:#否则
# 	print('努力赚钱吧')
# print('程序结束')


# 3-3 elif多条件判断
# money=230
# 错误示范
# if money>=100:
# 	print("恭喜你可以买宝马")
# if money>=50 and money<100:
# 	print('恭喜你可以买丰田')
# if money>=20 and money<50:
# 	print("恭喜你可以买二手车")
# else:
# 	print("共享单车了解一下")
# 运用elif多条件判断
# money=230
# if money>=100:
# 	print("恭喜你可以买宝马")
# elif money>=50 and money<100:
# 	print('恭喜你可以买丰田')
# elif money>=20 and money<50:
# 	print("恭喜你可以买二手车")
# else:
# 	print("共享单车了解一下")
# 特性：if写在开头且不能省略，只有一个。但elif可以有任意一个包括零个。
# else只有一个处在末尾且可以省略，在elif多条件判断中只执行第一个满足条件的语句


# 3-4 选择结构嵌套
# 注意事项；1.条件后的冒号不能省略 2.else后面不要写条件 3.缩进必须一致
# money=int(input('请输入存款金额（0-1000)?'))
# day=int(input('今天星期几(1-7)?'))
# if money>=100:
# 	print("恭喜你可以买宝马")
# 	if day<=5:
# 		print('周末去提车')
# 	else:
# 		print('今天下午去提车')
# elif money>=50 and money<100:
# 	print('恭喜你可以买丰田')
# elif money>=20 and money<50:
# 	print("恭喜你可以买二手车")
# else:
# 	print("共享单车了解一下")


# 3-5选择结构练习
# 练习一
# 1.星期一特价菜：水煮鱼
#   星期二特价菜：烧排骨
#   星期三，四特价菜：宫爆鸡丁
#   星期五，六特价菜：清蒸鲈鱼
#   其它：干锅肥肠
# 根据用户输入星期几，输出特价菜是什么？

# day=int(input('今天是星期几？(1-7)'))
# if day==1:
# 	print('水煮鱼')
# elif day==2:
# 	print('烧排骨')
# elif day==3 or day==4:
# 	print("宫爆鸡丁")
# elif day==5 or day==6:
# 	print("清蒸鲈鱼")
# elif day==7:
# 	print("干锅肥肠")
# else:
# 	print("请输入1-7")

# 练习二
# 根据输入判断学生的成绩等级，
# 如果成绩>=90分，则输出“优秀”;
# 如果成绩>=80分，则输出“良好”;
# 如果成绩>=60分，则输出“中等”;
# 否则，输出“差”

# score=int(input("请输入学生的分数："))
# if score>=90:
# 	print("你的成绩等级为：“优秀”")
# elif score>=80 and score<90:
# 	print("你的成绩等级为：“良好”")
# elif score>=60 and score<80:
# 	print("你的成绩等级为：“中等”")
# else:
# 	print("你的成绩等级为：“差”")

# 练习三
# 现在有一个银行保险柜，有两道密码。想拿到里面的钱必须两次输入的密码都要正确。
# 如果第一道密码都不正确，那直接把你拦在外面；
# 如果第一道密码输入正确，才能有权输入第二道密码。
# 只有当第二道密码也输入正确，才能拿到钱！(两道密码自己设)(嵌套if)

# 错解
# key1=2004
# key2=2005
# key=int(input("请输入第一道密码："))
# if key1==2004:
# 	print("恭喜你！答对了！")
# key=int(input("请输入第二道密码："))	
# if key2==2005:
# 	print("恭喜你！拿到钱了！")
# # else:
# # 	print("请输入第二道密码：")
# # 	key=int(input("请输入第二道密码："))
# # 	if key2==2005:
# # 		print("恭喜你！拿到钱了！")
# # 	else:
# # 		print("密码错误！")

# #正解
# key1='2004'
# key2='2005'
# key=input("请输入第一道密码：")
# if key==key1:
# 	print("恭喜你！密码正确！")
# 	key=input('请输入第二道密码：')
# 	if key==key2:
# 		print('恭喜你！密码正确！')
# 	else:
# 		print('密码错误！')
# else:
# 	print("密码错误！")

# 4.开发一个计算器，用户输入第一个数、加减乘除、第二个数，控制台显示计算结果。
# 较慢的方法
# word1=int(input("请输入第一个数："))
# word2=int(input('请输入第二个数：'))
# s=input('请输入符号（+ - * /）：')
# if s=='+':
# 	print(word1+word2)
# elif s=='-':
# 	print(word1-word2)
# elif s=='*':
# 	print(word1*word2)
# elif s=='/':
# 	print(word1/word2)
# #较快的方法
# word1=int(input('请输入第一个数：'))
# word2=int(input('请输入第二个数：'))
# s=input('请输入符号（+ - * /）：')
# result=0 #保存运算结果

# if s=='+':
# 	result=word1+word2
# elif s=='-':
# 	result=word1-word2
# elif s=='*':
# 	result=word1*word2
# elif s=='/':
# 	result=word1/word2
# print('计算结果:',result)


# 案例1：
# 为一家超市开发一个简易的收银系统(以3-5种商品为例): 
# 使用变量保存：商品编号 商品价格 商品名字

# 1.提示用户输入商品编号和数量,然后显示总价多少钱。
# 2.提示用户输入付款金额,然后显示找零金额。
# 错解
# a='001'
# b='002'
# c='003'
# s=int(input('请输入你所需要的商品代码：'))
# if s==a:
# 	print("你所选择的商品是：书本，价格是：2元")
# if s==b:
# 	print("你所选择的商品是：钢笔，价格是：5元")
# if s==c:
# 	print("你所选择的商品是：吉他，价格是：400元")

# 正解
# 进行配对，三个变量一一对应
# num1='001'
# price1=7.125
# name1='钢笔'

# num2='002'
# price2=5
# name2='本子'

# num3='003'
# price3=400
# name3='吉他'

# #提前声明变量保存需要的商品的价格和名称(可有可不有)
# price=0
# name=''
# #输入需要的值
# num=input('请输入商品编号')
# count=int(input('请输入商品数量'))
# #进行一一对应
# if num==num1:
# 	price=price1
# 	name=name1
# elif num==num2:
# 	price=price2
# 	name=name2
# elif num==num3:
# 	price=price3
# 	name=name3
# else:
# 	print("无此商品")
# #判断，若无此商品，则价格为零，那么对于计算找零，只需保证价格不为零即可
# if price!=0:#价格不等于零时
# 	amount=price*count#计算商品金额
# 	print('您当前购买的是：',name,'，单价：',price,'元，数量：',count,'金额：',round(amount,2),'元')

# 	money=float(input('请输入付款金额：'))
# 	if money<amount:
# 		print('金额不足！')
# 	else:
# 		print("付款",money,'元！''找零',round(money-amount,2),'元！')


# 3-8 round()函数（解决浮点型误差,保留指定的小数位）
# a=15.3
# b=3
# c=a/b
# print(c)
# print(round(c,1))
# print(round(3.1415926,3))
# print(round(3.1415926,5))
# 结构：round（需要保留的值，小数点后保留位数）


# 4-1 了解循环
# for x in range(10):
# 	print('hello word!')#循环操作：重复执行的业务


# 4-2 for循环语法构成
# for 变量名 in 序列：
#   循环语句

# 执行次数=序列中元素的个数
# for s in range(0,10):
# 	print('第',s,'次打印hello word!')

# 步长
# range(开始值，结束值（不包含），步长)
# for s in range(1,101,11):
# 	print(s)

# 将列表中的元素取出来
# for x in ['a','b']:
# 	print(x)


# 4-3 for循环的遍历容器
# 遍历：将容器中的数据一个一个取出来

# #直接遍历
# name=['张三','李四','王五','赵六']
# # for names in name:
# # 	print(names)
# #应用
# for names in name:
# 	if names=='王五':
# 		print('王五')

# 构造索引
# for x in range(0,4):
# 	print(name[x])

# 元组的直接遍历
# score=(67,48,165,1684,64,864,1,4381,531)
# for score in scores:
# 	print(score)
# 元组的构造索引
# score=(67,48,165,1684,64,864,1,4381,531)
# for x in range(0,len(score)):
# 	print(score[x])
# 求平均数
# total=0#设置这个是为了在后面计算的时候有个初始值，即total是从0开始计算
# for socres in score:
# 	total=total+socres
# print(total/len(score))

# 循环遍历字典只能获取键 只能直接遍历不能构造索取
dicta = {'name': '张三', 'age': '18', 'hobby': 'play'}
for x in dicta:
    print(x, dicta[x])

# 循环遍历集合只能获取无序的数据，只能直接遍历不能构造索取
# seta={1,16,513,53,44,57,62,6,22,34}
# for s in seta:
# 	print(s)


# 4-4 for循环例子和求和问题
# 大宝买车时，贷款12w，分10年还
# 1.循环操作是什么？---每年还1w2
# 2.循环的次数？---10次
# 求和问题
# total=0
# for year in range(1,11):
# 	total=total+1.2
# 	print('第',year,'年到了！累计已还',round(total,2),'万！还剩',round(12-total,2),'万！')

# 1到100间所有数求和
# total=0
# for x in range(1,101):
# 	total=total+x
# 	print(x)
# print(total)


# #4-5 最大值最小值问题
# scores=[45,615,1,531,65165,4,15,131,684]
# # #函数方法
# # print(max(lista))
# # print(min(lista))
# #循环方法:
# x=scores[0]
# for s in scores:
# 	if s>x:
# 		x=s#将更大值更新为最大值
# print(x)

# x=scores[0]
# for s in scores:
# 	if s<x:
# 		x=s#将更小值更新为最小值
# print(x)


# 4-6 while循环
# 通过判断条件来控制循环语句的执行
# while 判断条件：
#    执行语句
# i=0
# while i<=9:
# 	print('第',i,'次打印：hello word')
# 	i=i+1
# for适合循环次数确定的业务，可以直接遍历容器
# while适合已知循环执行条件的业务

# year=1
# while year<=10:
# 	print('第',year,'年，还款1.2w！')
# 	year=year+1

# #获取100到200间的偶数
# i=100
# while i<=200:
# 	print(i)
# 	i+=2


# #4-7 嵌套循环
# for year in range(1,11):
# 	print('******第',year,'年到了！')
# 	for x in range(1,13):
# 		print('第',x,'月到了！还款1000元')

# #遍历多维容器
# lista=[15205,465,13,1,561,31,354,651,5,13]
# listb=[16205,465,13,1,561,31,354,651,5,13]
# listc=[15205,465,13,1,561,31,354,651,5,14]
# listx=[lista,listb,listc]

# for x in listx:
# 	for s in x:
# 		print(s)


# 4-8 循环结构练习
# 1.用户输入任意10个数，for循环求他们的平均值；
# 自解
# num1=int(input("请输入第一个数字："))
# num2=int(input("请输入第二个数字："))
# num3=int(input("请输入第三个数字："))
# num4=int(input("请输入第四个数字："))
# num5=int(input("请输入第五个数字："))
# num6=int(input("请输入第六个数字："))
# num7=int(input("请输入第七个数字："))
# num8=int(input("请输入第八个数字："))
# num9=int(input("请输入第九个数字："))
# num10=int(input("请输入第十个数字："))
# num=[num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]
# total=0
# for x in num:
# 	total=total+x
# print(total/x)
# 正解：
# total=0
# for x in range(1,11):
# 	num=input('请输入'+str(x)+'一个数：')#input中使用+号进行拼接
# 	total+=num
# print(total/10)

# 用户输入任意10个数，for循环求他们的平均值；
# total=0
# count=1#计算一共循环了多少次（即一共输入了几个数）
# i=1
# while i<2:
# 	num=int(input("请输入第"+str(count)+"个数："))
# 	total+=num
# 	count+=1
# 	s=int(input("如果继续输入请输入：1，如果不想输入请输入：2:"))
# 	if s==2:
# 		i=10086
# print('总数为：',total,'输入了',count-1,'个数','平均值为:',total/(count-1))


# 2.一张纸的厚度大约是0.08mm，对折多少次之后能达到珠穆朗玛峰的高度（8844米）？
# t=0.08
# num=0
# while t<8844000:
# 	t=t*2
# 	num+=1
# 	print('第',num,'次折叠纸')

# 3.鸡兔同笼问题：今有鸡兔同笼，上有三十五个头，下有九十四足，问鸡兔各几只？
# 鸡有23只，兔有12只
# 运用到穷举法：列举所有的可能性，找到正确的结果
# 鸡的范围：0---35   兔的范围：35-鸡
# for j in range(0,36):
# 	t=35-j
# 	if j*2+t*4==94:
# 		print(j,t)


# 4.我国古代数学家张邱建在《算经》中出了一道“百钱买百鸡”的问题，
# 题意是这样的：5文钱可以买一只公鸡，3文钱可以买一只母鸡，1文钱可以买3只雏鸡。
# 现在用100文钱买100只鸡，那么各有公鸡、母鸡、雏鸡多少只？请编写程序实现。
# 公鸡的范围：0---20 母鸡的范围为0---33  雏鸡的范围0---100
# for gj in range(0,21):
# 	for mj in range(0,34):
# 		for cj in range(0,101):
# 			if gj+cj+mj==100 and gj*5+mj*3+cj/3==100:
# 				print(gj,mj,cj)

# 雏鸡的数量=100-公鸡-母鸡
# for gj in range(0,21):
# 	for mj in range(0,34):
# 		cj=100-gj-mj
# 		if gj+cj+mj==100 and gj*5+mj*3+cj/3==100:
# 			print(gj,mj,cj)


# 4-11 break和continue
# break：结束整个循环操作
# continue：结束本次循环，继续下次循环
# for year in range(1,11):
# 	if year==5:
# 		print("第五年疫情原因，今年不用还款了！")
# 		continue
# 	if year==6:
# 		print("第",year,"到了！还款2.4w！")
# 		continue
# 	if year==8:
# 		print("第8年，提前还清，以后都不用还了！")
# 		break
# 	print("第",year,"年到了！还款1.2w！")


# 案例：模拟银行ATM存款取款

# 1.模拟3张银行卡,1001,1002,1003,分别设置密码和余额(使用列表嵌套字典的方式)；

# 2.提示用户输入银行卡和密码，遍历每张卡的信息验证是否成功；


# 3.如果用户输入正确---提示让用户选择取款.存款还是退出,并提示余额多少.  输入错误---重新输入卡号密码；

# 选择取款---提示输入取款额度,如果超过余额,提示余额不足;否则,在余额上减掉相应金额；

# 选择存款---输入存款额度,余额加上相应额度,并提示余额多少；

# 选择退出---重新登录；

# 4.设置3次输入错误账号密码,提示银行卡已被锁定，程序结束。

# card1={'姓名':'张三','卡号':'1001','密码':123,'余额':10000}
# card2={'姓名':'李四','卡号':'1002','密码':123123,'余额':10000}
# card3={'姓名':'王五','卡号':'1003','密码':123789,'余额':10000}
# card4={'姓名':'赵六','卡号':'1004','密码':123456,'余额':10000}
# lista=[card1,card2,card3,card4]
# false=0
# while 1==1:
# 	name=input('请输入你的卡号：')
# 	num=int(input('请输入你的密码：'))
# 	msg=0#用msg表示登录状态，若为0则未登录，为1则为登录
# 	for card in lista:
# 		if name==card['卡号'] and num==card['密码']:
# 			msg=1
# 			false=0
# 			print('恭喜你！',card['姓名'],'登录成功！')
# 	if msg==0:
# 		false+=1
# 		if false==3:
# 			print('您已经连续输入错误三次，银行卡已被锁定！')
# 			break
# 		else:
# 			print('不好意思，你已经连续',false,'次输入错误，还有',3-false,'次银行卡将会被锁定！')
# 			continue
# 	while 2==2:
# 		w=int(input('请输入你想要办理的业务：1.存款 2.取款 3.退出：'))
# 		if w==1:
# 			print('你的存款还有',card['余额'],'元!')
# 			cun=float(input('请输入你需要存款多少：'))
# 			if cun<=0:
# 				print('不好意思，请重新存款！')
# 				continue
# 			for card in lista:
# 				if name==card['卡号']:
# 					card['余额']+=cun
# 					print('存款了',cun,'元！','您的存款为',card['余额'],'元！')
# 		elif w==2:
# 			print('你的存款还有',card['余额'],'元!')
# 			qu=float(input('请输入你需要取款多少：'))
# 			if qu<=0 or qu>card['余额']:
# 				print('不好意思，请重新取款！')
# 				continue
# 			for card in lista:
# 				card['余额']=card['余额']-qu
# 			print('取款了',qu,'元！','您的取款为',card['余额'],'元！')
# 		elif w==3:
# 			print('--------已退出------------')
# 			break
# 		else :
# 			print('您所选择的业务不在服务范畴内，请重新选择业务！')
# 			continue


# #4-16 冒泡排序
# #总轮数=列表长度-1
# #每轮比较次数=列表长度-轮数
# lista=[1,84,51,7,87]
# for a in range(1,len(lista)-1+1):#进行轮数间的比较
# 	#print('第',a,'轮比较')
# 	for b in range(0,len(lista)-a-1+1):#进行轮数间中次的比较
# 		#print(b,'----',b+1)
# 		if lista[b]>=lista[b+1]:#降序只需更改符号即可
# 			#两个数交换值的过程
# 			c=lista[b]
# 			lista[b]=lista[b+1]
# 			lista[b+1]=c
# print(lista)


# 5-1 函数
# 调用函数：函数名（参数列表）英文括号
# 自动排序函数：sorted
# lista=[15,15,153,465,4684,84,53,4,684,6]
# nwelista=sorted(lista)
# print(nwelista)


# 5-2 常见内置函数
# 排序函数：升序和降序
# 升序：
# lista=[15,15,153,465,4684,84,53,4,684,6]
# nwelista=sorted(lista)
# print(nwelista)
# 降序：
# lista=[15,15,153,465,4684,84,53,4,684,6]
# nwelista=sorted(lista,reverse=True)  #reverse代表反转，即降序
# print(nwelista)

# 最值函数：最大值和最小值
# 最大值函数：max  print(max(lista))
# 最小值函数：min  print(min(lista))

# 长度函数：获取某一个序列的长度
# 表示：len(lista)

# 求和函数：进行序列间的求和
# 函数(sum)
# print(sum(lista))
# 求平均值：print(sum(lista)/len(lista))

# 反转序列函数
# 函数：reversed
# newlist=reversed(lista)
# for x in newlist:
# 	print(x)

# 获取变量id
# 函数：id(用于判断两个的值是否相同)
# a=5
# b=5
# c=10
# print(id(a))

# #二进制的转化
# # 函数：bin
# a=12
# b=bin(a)
# print(b)


# 5-3 自定义函数
# 第一步：定义一个函数
# 第二部：调用一个函数
# 语法：
# def square(x):#'def'关键字 'square'函数命名可自定义 '(x)'为输入参数
# 	s=x*x      #函数的主体，进行操作
# 	return s   #若有结果返回变量，无结果可以不用此行
# #例子(无参数)：第一步定义函数：
# def function1():
# 	print('hello word')
# #第二步调用函数
# function1()
# for x in range(10):
# 	function1()
# #例子（有参数）：第一步定义函数：
# def getSum(a,b):#形式上的参数（无具体意义，方便我们构建函数具体执行的内容）
# 	result=a+b
# 	print('相加的结果是：',result)
# # #第二步调用函数
# getSum(4,5)#实参 实参与形参的个数必须一致


# #5-4 参数与返回值
# #返回值：函数执行后被返回的结果
# #返回单个值
# def fun1():
# 	print('fun1被执行了！')
# 	a=1
# 	return a#返回值
# num=fun1()#赋一个变量去接受返回值
# print(num)
# #返回多个值
# def fun2():
# 	print('fun2被执行了！')
# 	a=1
# 	b=2
# 	c=3
# 	return a,b,c#用逗号进行分隔
# num1,num2,num3=fun2()#有几个变量就赋几个变量去接受返回值
# print(num1,num2,num3)


# #例子：榨汁机
# def z(f):
# 	print("榨汁ing")
# 	result=f+"汁"
# 	return result#返回rusult
# zhi=z('西瓜')#接受result
# print(zhi)


# 5-5 变量作用域
# #变量作用域的定义：表示一个变量起作用的范围
# a=2#全局变量（定义在函数或者类的外部）
# def function():
# 	a=100#创建了一个同名的局部变量a
# 	print(a)#优先获取函数内部的局部变量a，而不是全局变量a
# 	b=6#局部变量（定义在函数或者类的内部）
# 	print(b)
# function()
# print(a)
# #全局变量：可以在整个文件中被访问，函数内部不能给全局变量重新赋值
# #局部变量：只能在函数或类的内部被访问

# 将函数内部的同名变量变为全局的同名变量方法：
# a='北京'
# def function():
# 	global a  #将函数内部的a设置为全局变量
# 	a='上海'
# 	print(a)
# function()
# print(a)


# 函数练习

# 1.写函数，接收3个数字参数，返回最大的那个数字。
# def function(a,b,c):
# 	d=max(a,b,c) 
# 	return d
# e=function(6,4,5)
# print(e)

# 2.编写一个用户登录函数（用户名密码提前设置）；
# 返回用户登录成功或者失败的结果；
# name=111
# key=666
# def function():
# 	msg="失败"
# 	uname=int(input('请输入你的账号：'))
# 	ukey=int(input('请输入你的密码：'))
# 	if uname==name and ukey==key:
# 		print('登录成功！')
# 		msg="成功"
# 	else:
# 		print('登陆失败')
# 	return msg#函数一旦执行到return就会停止
# t=function()
# print(t)

# 3.做一个分数统计器：
# 函数中让用户循环输入一组分数，输入结束后保存到一个列表中。
# 把平均分，最高分，最低分，及格人数，及格率返回出来（接收列表为参数）。
# #自解
# i=1
# def function():
# 	p=0
# 	ma=0
# 	mi=0==
# 	hl=0
# 	hp=0
# 	al=0
# 	score=[]
# 	while i<2:
# 		s=int(input('请输入学生的分数：'))
# 		al+=1
# 		score.append(s)
# 		if s>=60:
# 			hp+=1
# 		ask=int(input('请输入是否继续输入学生分数，如果是，请按1，否则请按2：'))
# 		if ask==1:
# 			continue
# 		else:
# 			print("已结束输入学生成绩")
# 			break
# 	p=sum(score)/len(score)
# 	ma=max(score)
# 	mi=min(score)
# 	hl=hp/len(score)
# 	return p,ma,mi,hl,hp
# p,ma,mi,hl,hp=function()
# print('平均分是：',p,'分 最高分是：',ma,'分 最低分是：',mi,'分 平均率是：',hl,'% 合格人数是：',hp,'人')

# #正解
# def function():
# 	avgscore=0
# 	maxscore=0
# 	minscore=0
# 	passcount=0
# 	passpercent=0
# 	scorelist=[]
# 	totalcount=0
# 	while 1==1:
# 		s=int(input('请输入学生的分数：'))
# 		totalcount+=1
# 		scorelist.append(s)
# 		if s>=60:
# 			passcount+=1
# 		c=int(input('请输入是否继续输入学生分数，如果是，请按1，否则请按2：'))
# 		if c==2:
# 			break
# 	avgscore=sum(scorelist)/len(scorelist)
# 	maxscore=max(scorelist)
# 	minscore=min(scorelist)
# 	passpercent=passcount/len(scorelist)
# 	return avgscore,maxscore,minscore,passpercent
# avgscore,maxscore,minscore,passpercent=function()
# print(avgscore,maxscore,minscore,passpercent)


# #5-7 return的另外一种用法
# #嵌套循环终止问题
# for x in range(1, 11):
# 	print('_____第', x, '年！_____')
# 	for y in range(1, 13):
# 		print('第', x, '年！，第', y, '月！')
# 		if x == 5 and y == 5:
# 			break  # 此处的break只能停止离break最近的循环
# #逻辑方面解决整套循环终止问题
# msg=0#引入一个变量进行判断
# for x in range(1,11):
# 	print('_____第',x,'年！_____')
# 	for y in range(1,13):
# 		print('第',x,'年！，第',y,'月！')
# 		if x==5 and y==5:
# 			msg=1
# 			break
# 	if msg==1:
# 		break
# #利用函数解决整套循环终止问题
# def function():
#     for x in range(1, 11):
#         print('_____第', x, '年！_____')
#         for y in range(1, 13):
#             print('第', x, '年！，第', y, '月！')
#             if x == 5 and y == 5:
#                 return  # 此时ruturn直接终止了整个自定义函数，自然就将嵌套循环一并结束
#
#
# function()


# 大宝的超市开业了，为了更好的管理商品信息，准备开发一个商品管理系统。
# 系统需要用户先登录，再进行操作，其中包含以下功能菜单:
# 1.显示商品列表 2.增加商品信息 3.删除商品 4.设置商品折扣 5.修改商品信息 6.退出
# a.	使用列表嵌套字典的方式保存用户数据（包含用户名，密码，姓名）；
# b.	使用列表嵌套字典的方式保存商品数据（包含编号，名称，价格，折扣）；
# c.	编写用户登录的函数，返回登录结果；
# d.	循环提示菜单，业务完毕时返回主菜单，退出时回到登陆页面；
# e.	将功能菜单中的业务功能各自编写到函数中；
# f.	用户选择不同业务编号时，调用已经写好的各种函数。

card1 = {'姓名': '张三', '账号': 1001, '密码': 123123}
card2 = {'姓名': '李四', '账号': 1002, '密码': 123456}
card3 = {'姓名': '王五', '账号': 1003, '密码': 123789}
lista = [card1, card2, card3]
goods1 = {'名称': '苹果', '编号': '1001', '价格': '10', '折扣': 1}
goods2 = {'名称': '香蕉', '编号': '1002', '价格': '8', '折扣': 1}
goods3 = {'名称': '橙子', '编号': '1003', '价格': '15', '折扣': 1}
goods4 = {'名称': '橘子', '编号': '1004', '价格': '9', '折扣': 1}
listb = [goods1, goods2, goods3, goods4]


# 登陆界面
def func0():
    while 1 == 1:
        user = int(input("请输入你的账号:"))
        key = int(input("请输入你的密码:"))
        for list in lista:
            if user == list["账号"] and key == list["密码"]:
                print("================登录成功！", list["姓名"], "===================")
                return "登录成功！"
        else:
            print("账号或密码错误！登陆失败！请重新登录！")
            print("==============================")
            continue


# 显示界面
def func1():
    print("显示商品列表")
    for list in listb:
        print(list)


# 增加界面
def func2():
    while 3 == 3:
        lista = []
        for list in listb:
            lista.append(int(list["编号"]))
            num = max(lista) + 1
        name = input("你增加的商品的名称:")
        price = (input("你增加的商品的价格:"))
        kou = int(input("你增加的商品的折扣:"))
        goods = {"名称": name, "编号": num, "价格": price, "折扣": kou}
        listb.append(goods)
        print("=============商品信息添加成功！================")
        func3()
        func2()


# 删除商品信息(通过编号进行删除)
def func3():
    s = 0
    while 3 == 3:
        name = input("请输入你要删除的名称:")
        msg = 0
        for list in listb:
            if name == list["名称"]:
                print("---------即将删除", list["名称"], "信息---------")
                listb.remove(list)  # 利用remove 删除循环中的列表
                print("------------删除成功-------")
                msg == 100
                func3()
                break
        if msg == 0:
            if s <= 1:
                print("你输入的商品不存在！请重新输入！")
                s += 1
                print("你已经连续", s, "次输入错误了！还剩", 3 - s, "次机会！")
                continue
            elif s >= 2:
                print("你已经连续三次输入错误了！，系统自动帮你退出界面！")
                func2()


# 设置商品折扣
def func4():
    while 3 == 3:
        name = input("请输入你要修改的名称:")
        for list in listb:
            if name == list["名称"]:
                kou = int(input("请输入你要修改后的折扣:"))
                list["折扣"] = kou
                print("修改完成")
                func1()
                func2()


# 修改界面
def func5():
    while 3 == 3:
        name = input("请输入你要修改的名称:")
        for list in listb:
            if name == list["名称"]:
                print("你想要修改的项目是（1.名称 2.编号 3.价格 4.折扣 5.退出）")
                num = int(input("请输入你要修改的项目的编号:"))
                if num == 1:
                    names = input("请输入你要修改后的名称:")
                    list["名称"] = names
                    print("修改完成")
                    func2()
                elif num == 2:
                    nums = int(input("请输入你要修改后的编号:"))
                    list["编号"] = nums
                    print("修改完成")
                    func2()
                elif num == 3:
                    price = int(input("请输入你要修改后的价格:"))
                    list["价格"] = price
                    print("修改完成")
                    func2()
                elif num == 4:
                    kou = int(input("请输入你要修改后的折扣:"))
                    list["折扣"] = kou
                    print("修改完成")
                    func2()
                elif num == 5:
                    func2()
                else:
                    print("你所输入的不符合要求！请重新输入！")
                    continue


# 主界面
def func6():
    while 2 == 2:
        print("----------------菜单栏--------------------")
        print("--------------1.显示商品列表---------------")
        print("--------------2.增加商品信息---------------")
        print("--------------3.删除商品------------------")
        print("--------------4.设置商品折扣---------------")
        print("--------------5.修改商品信息---------------")
        print("--------------6.退出----------------------")
        num = int(input("请输入你要操作的数字:"))
        if num == 1:
            func1()
        elif num == 2:
            func2()
        elif num == 3:
            func3()
        elif num == 4:
            func4()
        elif num == 5:
            func5()
        elif num == 6:
            print("正在退出.......")
            print("================================")
            func1()
            continue


func6()


def main():
    print("1.添加学生 ")
    print("2.删除学生 ")
    print("3.修改学生信息 ")
    print("4.查询单个学生信息 ")
    print("5.查询所有学生信息 ")
    print("6.退出系统 ")


def load():
    global stu_list
    if os.path.exists('student.txt'):
        f = open("student.text", "r", encoding="utf-8")
        buf = f.read()
        if buf:
            stu_list = eval(buf)
        f.close()


def save():
    f = open("student.text", "w", encoding="utf-8")
    f.write(str(stu_list))
    f.close()
    os.chdir('../')


def information():
    name = input("请输入学生的姓名:")
    for stu in stu_list:
        if name == stu["name"]:
            print("-------------不添加-------------")
            return
    age = input("请输入学生的年龄:")
    gender = input("请输入学生的性别:")
    stu_dict = {"name": name, "age": int(age), "gender": gender}
    stu_list.append(stu_dict)
    print(stu_list)
    print("==================学生信息添加成功==================")


def hello():
    name = input("请输入学生的姓名:")
    for stu in stu_list:
        if name == stu["name"]:
            stu_list.remove(stu)
            print("==========该学生信息已被删除！============")
            return
    else:
        print("==================无该生信息！==================")


def change():
    name = input("请输入学生的姓名:")
    stu: object
    for stu in stu_list:
        if name == stu["name"]:
            while 2 == 2:
                choice = int(input("请选择你要修改的内容（1.姓名 2.年龄 3.性别）:"))
                if choice == 1:
                    names = input("请输入你修改后学生的名字:")
                    stu["name"] == names
                    y = int(input("你是否还要修改信息（1.需要 2.不需要）："))
                    if y == 1:
                        continue
                    else:
                        break
                elif choice == 2:
                    ages = input("请输入你修改后学生的年龄:")
                    stu["age"] == ages
                    y = int(input("你是否还要修改信息（1.需要 2.不需要）："))
                    if y == 1:
                        continue
                    else:
                        break
                elif choice == 3:
                    genders = input("请输入你修改后学生的年龄:")
                    stu["gender"] == genders
                    y = int(input("你是否还要修改信息（1.需要 2.不需要）："))
                    if y == 1:
                        continue
                    else:
                        break
                else:
                    print("你输入的无效，请重新输入！")
                    continue


def one():
    name = input("请输入学生的姓名:")
    for stu in stu_list:
        if name == stu["name"]:
            print("这名学生的信息是：", stu)
            return


def suoyou():
    if len(stu_list) > 0:
        for student in stu_list:
            print(student)


def zhu():
    load()
    while 1 == 1:
        main()
        num = int(input("去请选择要进行的操作编号："))
        if num == 1:
            print("添加学生")
            information()
        elif num == 2:
            print("删除学生")
            hello()
        elif num == 3:
            print("修改学生信息")
            change()
        elif num == 4:
            print("查询单个学生信息")
            one()
        elif num == 5:
            print("查询所有学生信息")
            suoyou()
        elif num == 6:
            print("退出系统")
            save()
            zhu()
        else:
            print("输入有误！请重新输入！")
            continue


zhu()

# 实例：蟒的画法
import turtle

turtle.setup(650, 350, 200, 20)
turtle.penup()  # turtle.penup（）意思为将画笔拿起来，即小海龟在空中飞行
turtle.fd(-250)  # 向前行走-250个像素单位
turtle.pendown()  # turtle.pendown（）意思为将画笔放下来，即小海龟在地上行走
turtle.pensize(25)  # turtle.penside(width)意思是控制画笔的大小，即小海龟的腰围
turtle.pencolor("purple")  # turtle。pencolor（color）意思是改变画笔的颜色，即小海龟的颜色
turtle.seth(-40)  # turtle.seth意为改变行进方向，即改变海龟的方向，该方向为绝对坐标轴中的角度方向
for i in range(4):
    turtle.circle(40, 80)  # turtle。circle(r,extent=None)意为根据半径为r绘制extent角度的弧形
    turtle.circle(-40, 80)  # r：默认圆心在海归左侧r距离的位置   extent：绘制角度，默认是360度整圆
turtle.circle(40, 80 / 2)
turtle.fd(40)
turtle.circle(16, 100)
turtle.fd(40 * 2 / 3)
turtle.done()
# 教程：关于turtle库
# turtle.setup(width,height,stratx,strat_y)
# setup()设置窗体的大小及位置，其中四个参数后两个可选，除非特殊需要，一般不使用setup函数
# stratx和strat_y两个参数是窗口哦到电脑屏幕左上角的距离
# width和height两个参数是指窗口的大小，一般不用改
# turtle.left(angle)和turtle.right(angle)意为在海龟当前的方向向左或向右旋转angle角度
