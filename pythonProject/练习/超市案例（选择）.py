# 案例1：
# 为一家超市开发一个简易的收银系统(以3-5种商品为例):
# 使用变量保存：商品编号 商品价格 商品名字

# 1.提示用户输入商品编号和数量,然后显示总价多少钱。
# 2.提示用户输入付款金额,然后显示找零金额。
#错解
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

#正解
#进行配对，三个变量一一对应
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