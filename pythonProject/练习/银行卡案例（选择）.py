# 练习三
# 现在有一个银行保险柜，有两道密码。想拿到里面的钱必须两次输入的密码都要正确。
# 如果第一道密码都不正确，那直接把你拦在外面；
# 如果第一道密码输入正确，才能有权输入第二道密码。
# 只有当第二道密码也输入正确，才能拿到钱！(两道密码自己设)(嵌套if)

#错解
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