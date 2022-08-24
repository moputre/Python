#5-3 自定义函数
#第一步：定义一个函数
#第二部：调用一个函数
#语法：
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
