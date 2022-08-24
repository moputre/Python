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