def denglu():
    while 1 == 1:
        card1 = {'姓名': '张三', '账号': 1001, '密码': 123123}
        card2 = {'姓名': '李四', '账号': 1002, '密码': 123456}
        card3 = {'姓名': '王五', '账号': 1003, '密码': 123789}
        lista = [card1, card2, card3]
        names = int(input("请输入你的登录账号："))
        key = int(input('请输入你的账号密码：'))
        msg = 0
        false = 0
        for list in lista:
            if names == list["账号"] and key == list["密码"]:
                i = "登录成功"
                return i
                msg = 1
        if msg == 0:
            false += 1
            if false == 3:
                print('您已经连续输入错误三次，银行卡已被锁定！')
                break
            else:
                print('不好意思，你已经连续', false, '次输入错误，还有', 3 - false, '次银行卡将会被锁定！')
                continue


f = denglu()
print(f)

# if msg == 0:
#     false += 1
#     if false == 3:
#         print("您已连续输错3次，系统锁定！")
#         break
#     else:
#         print("请重新输入，且你已经连续输错了", false, "次,还有", 3 - false, "次机会")
#         continue
