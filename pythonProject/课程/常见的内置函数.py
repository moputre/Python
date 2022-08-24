#5-2 常见内置函数
#排序函数：升序和降序
#升序：
# lista=[15,15,153,465,4684,84,53,4,684,6]
# nwelista=sorted(lista)
# print(nwelista)
#降序：
# lista=[15,15,153,465,4684,84,53,4,684,6]
# nwelista=sorted(lista,reverse=True)  #reverse代表反转，即降序
# print(nwelista)

#最值函数：最大值和最小值
#最大值函数：max  print(max(lista))
#最小值函数：min  print(min(lista))

#长度函数：获取某一序列的长度
#表示：len(lista)

#求和函数：进行序列间的求和
#函数(sum)
# print(sum(lista))
# 求平均值：print(sum(lista)/len(lista))

#反转序列函数
#函数：reversed
# newlist=reversed(lista)
# for x in newlist:
# 	print(x)

#获取变量id
#函数：id(用于判断两个的值是否相同)
# a=5
# b=5
# c=10
# print(id(a))

# #二进制的转化
# # 函数：bin
# a=12
# b=bin(a)
# print(b)