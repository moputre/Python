#4-4 for循环例子和求和问题
#大宝买车时，贷款12w，分10年还
#1.循环操作是什么？---每年还1w2
#2.循环的次数？---10次
#求和问题
# total=0
# for year in range(1,11):
# 	total=total+1.2
# 	print('第',year,'年到了！累计已还',round(total,2),'万！还剩',round(12-total,2),'万！')

#1到100间所有数求和
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