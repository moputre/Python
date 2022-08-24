# 1.用户输入任意10个数，for循环求他们的平均值；
#自解
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
#正解：
# total=0
# for x in range(1,11):
# 	num=input('请输入'+str(x)+'一个数：')#input中使用+号进行拼接
# 	total+=num
# print(total/10)

#用户输入任意10个数，for循环求他们的平均值；
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