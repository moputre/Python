# 4-3 for循环的遍历容器
# 遍历：将容器中的数据一个一个取出来

# 直接遍历
name = ['张三', '李四', '王五', '赵六']
# for names in name:
#     print(names)
# #应用
# for names in name:
# 	if names=='王五':
# 		print('王五')

# 构造索引
# for x in range(0, 4):
#     print(name[x])

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
