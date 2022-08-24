card1 = {'姓名': '张三', '账号': 1001, '密码': 123123}
card2 = {'姓名': '李四', '账号': 1002, '密码': 123456}
card3 = {'姓名': '王五', '账号': 1003, '密码': 123789}
lista = [card1, card2, card3]
goods1 = {'名称': '苹果', '编号': '1001', '价格': '10', '折扣': 1}
goods2 = {'名称': '香蕉', '编号': '1002', '价格': '8', '折扣': 1}
goods3 = {'名称': '橙子', '编号': '1003', '价格': '15', '折扣': 1}
goods4 = {'名称': '橘子', '编号': '1004', '价格': '9', '折扣': 1}
listb = [goods1, goods2, goods3, goods4]

while 1 == 1:
    user = int(input("请输入你的账号:"))
    key = int(input("请输入你的密码:"))
    for list in lista:
        if user == list["账号"] and key == list["密码"]:
            print("================登录成功！===================")
            while 2 == 2:
                print("----------------菜单栏--------------------")
                print("--------------1.显示商品列表---------------")
                print("--------------2.增加商品信息---------------")
                print("--------------3.删除商品------------------")
                print("--------------4.设置商品折扣---------------")
                print("--------------5.修改商品信息---------------")
                print("--------------6.退出----------------------")
                num = int(input("请输入你要操作的数字:"))
                if num == 1:
                    print("显示商品列表")
                    for list in listb:
                        print(list)
                elif num == 2:
                    name = input("你增加的商品的名称:")
                    num = (input("你增加的商品的编号"))
                    price = (input("你增加的商品的价格:"))
                    kou = int(input("你增加的商品的折扣:"))
                    goods = {"名称": name, "编号": num, "价格": price, "折扣": kou}
                    listb.append(goods)
                    print("=============商品信息添加成功！================")
                    continue
                elif num == 3:
                    name = input("请输入你要删除的名称:")
                    for list in listb:
                        if name == list["名称"]:
                            pass
                        continue
                elif num == 4:
                    pass
                elif num == 5:
                    while 3 == 3:
                        name = input("请输入你要修改的名称:")
                        for list in listb:
                            if name == list["名称"]:
                                print("你想要修改的项目是（1.名称 2.编号 3.价格 4.折扣 5.退出）")
                                num = int(input("请输入你要修改的项目的编号:"))
                                if num == 1:
                                    names = input("请输入你要修改后的名称:")
                                    list["名称"] = names
                                    print("修改完成")
                                    continue
                                elif num == 2:
                                    nums = int(input("请输入你要修改后的编号:"))
                                    list["编号"] = nums
                                    print("修改完成")
                                    continue
                                elif num == 3:
                                    price = int(input("请输入你要修改后的价格:"))
                                    list["价格"] = price
                                    print("修改完成")
                                    continue
                                elif num == 4:
                                    kou = int(input("请输入你要修改后的编号:"))
                                    list["折扣"] = kou
                                    print("修改完成")
                                    continue
                                elif num == 5:
                                    continue
                                else:
                                    print("你所输入的不符合要求！请重新输入！")
                                    continue
                elif num == 6:
                    print("正在退出.......")
                    print("================================")
                    continue
    else:
        print("账号或密码错误！登陆失败！请重新登录！")
        print("==============================")
        continue
