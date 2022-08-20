# 3.做一个分数统计器：
# 函数中让用户循环输入一组分数，输入结束后保存到一个列表中。
# 把平均分，最高分，最低分，及格人数，及格率返回出来（接收列表为参数）。
# #自解
# i=1
# def function():
# 	p=0
# 	ma=0
# 	mi=0==
# 	hl=0
# 	hp=0
# 	al=0
# 	score=[]
# 	while i<2:
# 		s=int(input('请输入学生的分数：'))
# 		al+=1
# 		score.append(s)
# 		if s>=60:
# 			hp+=1
# 		ask=int(input('请输入是否继续输入学生分数，如果是，请按1，否则请按2：'))
# 		if ask==1:
# 			continue
# 		else:
# 			print("已结束输入学生成绩")
# 			break
# 	p=sum(score)/len(score)
# 	ma=max(score)
# 	mi=min(score)
# 	hl=hp/len(score)
# 	return p,ma,mi,hl,hp
# p,ma,mi,hl,hp=function()
# print('平均分是：',p,'分 最高分是：',ma,'分 最低分是：',mi,'分 平均率是：',hl,'% 合格人数是：',hp,'人')

# #正解
# def function():
# 	avgscore=0
# 	maxscore=0
# 	minscore=0
# 	passcount=0
# 	passpercent=0
# 	scorelist=[]
# 	totalcount=0
# 	while 1==1:
# 		s=int(input('请输入学生的分数：'))
# 		totalcount+=1
# 		scorelist.append(s)
# 		if s>=60:
# 			passcount+=1
# 		c=int(input('请输入是否继续输入学生分数，如果是，请按1，否则请按2：'))
# 		if c==2:
# 			break
# 	avgscore=sum(scorelist)/len(scorelist)
# 	maxscore=max(scorelist)
# 	minscore=min(scorelist)
# 	passpercent=passcount/len(scorelist)
# 	return avgscore,maxscore,minscore,passpercent
# avgscore,maxscore,minscore,passpercent=function()
# print(avgscore,maxscore,minscore,passpercent)