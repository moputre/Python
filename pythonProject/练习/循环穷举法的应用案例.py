# 3.鸡兔同笼问题：今有鸡兔同笼，上有三十五头，下有九十四足，问鸡兔各几只？
#鸡有23只，兔有12只
#运用到穷举法：列举所有的可能性，找到正确的结果
#鸡的范围：0---35   兔的范围：35-鸡
# for j in range(0,36):
# 	t=35-j
# 	if j*2+t*4==94:
# 		print(j,t)


# 4.我国古代数学家张邱建在《算经》中出了一道“百钱买百鸡”的问题，
#题意是这样的：5文钱可以买一只公鸡，3文钱可以买一只母鸡，1文钱可以买3只雏鸡。
#现在用100文钱买100只鸡，那么各有公鸡、母鸡、雏鸡多少只？请编写程序实现。
#公鸡的范围：0---20 母鸡的范围为0---33  雏鸡的范围0---100
# for gj in range(0,21):
# 	for mj in range(0,34):
# 		for cj in range(0,101):
# 			if gj+cj+mj==100 and gj*5+mj*3+cj/3==100:
# 				print(gj,mj,cj)

#雏鸡的数量=100-公鸡-母鸡
# for gj in range(0,21):
# 	for mj in range(0,34):
# 		cj=100-gj-mj
# 		if gj+cj+mj==100 and gj*5+mj*3+cj/3==100:
# 			print(gj,mj,cj)
