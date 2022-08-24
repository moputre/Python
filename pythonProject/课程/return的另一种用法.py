# #5-7 return的另外一种用法
# #嵌套循环终止问题
# for x in range(1,11):
# 	print('_____第',x,'年！_____')
# 	for y in range(1,13):
# 		print('第',x,'年！，第',y,'月！')
# 		if x==5 and y==5:
# 			break#此处的break只能停止离break最近的循环
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
# 	for x in range(1,11):
# 		print('_____第',x,'年！_____')
# 		for y in range(1,13):
# 			print('第',x,'年！，第',y,'月！')
# 			if x==5 and y==5:
# 				return#此时ruturn直接终止了整个自定义函数，自然就将嵌套循环一并结束
# function()