# 用户输入年龄，如果年龄超过60岁，输出：可以退休了。
# age = int(input("请输入你的年龄："))
# if age >= 60:
#     print("可以退休了！")
# else :
#     print("继续努力吧！")


# 用户输入年龄，按照如下标准书写程序，判断用户处于哪个年龄阶段，并提示：您的年龄是xx: 青少年/青年/中年/老年。
# 年龄段划分标准：0-17岁为青少年；18-35岁为青年；36-59为中年，60-99岁为老年。
# age = int(input("请输入你的年龄："))
# if 0 < age <= 17:
#     print(f"你的年龄是{age}：青少年")
# elif 17 < age <= 35:
#     print(f"你的年龄是{age}：青年")
# elif 35 < age <= 59:
#     print(f"你的年龄是{age}：中年")
# else :
#     print(f"你的年龄是{age}:老年")


# 坐公交：假设坐公交需要买票上车，书写程序要求如下：
# 1.如果有票则可以上车，否则不能上车
# 2.上车后，如果有座位可以坐下，否则不能坐下。
# 已有程序如下，请补 全程序：
# ticket取值为1表示有票，取值为0表示无票
# import random

# ticket = 1
# seat取值为1表示有座位，取值为0表示无座位
# seat = 1
# if ticket == 1:
#     print("你可以上车！")
#     if seat == 1:
#         print("有座位！请入座！")
#     else :
#         print("没有座位！站着吧！")
# else :
#     print("你没有票！不能上车！")


# 用户登录输入验证码，已知验证码是axyz, 验证码正确可以登录，否则输出：验证码错误。
# num = input("请输入验证码：")
# key = "axyz"
# if num == key :
#     print("验证成功！已登录！")
# else :
#     print("验证码错误！，验证失败！无法登录！")


# 制作用户登录系统：已知A用户注册的用户名为aaa，密码是123456。具体要求如下：
# 登录时需要验证用户名、密码、验证码(固定验证码为qwer)。
# 提示：系统先验证验证码是否正确，正确后再验证用户名和密码。
# usera = "aaa"
# keya = 123456
# a = 'qwer'
# word = input("请输入你的验证码:")
# if a == word :
#     print("验证码正确！验证成功！")
#     user = input("请输入你的用户名:")
#     key = int(input("请输入你的密码:"))
#     if key == keya and user == usera:
#         print("账号密码正确！登录成功！")
#     else :
#         print("你的账号或密码错误！登陆失败！")
# else :
#     print("验证码错误！验证失败！")


# 设计"过7 游戏” 程序,即在 1- 99 之间的数字中,如果数字 包含 7 或者是 7 的倍数,则输出"过...", 否则输出 具体的数字.
# for i in range(1,100):
#     if i % 7 == 0 or i % 10 ==7 or i // 10 == 7:
#         print("过...")
#     else :
#         print(i)


# 编写代码模拟用户登陆。要求：用户名为 python，密码 123456，如果输入正确，打印“欢迎光临”，程序结束，如果输入错误，提示用户输入错误并重新输入
# while 1==1:
#     num = input("请输入你的用户名：")
#     key = int(input("请输入你的密码："))
#     num1 = "python"
#     key1 = 123456
#     if num == num1 and key ==key1:
#         print("欢迎光临！")
#         break
#     else :
#         print("用户名或密码错误！请重新输入！")
#         continue


# 猜数字游戏：电脑产生（1-100）的随机数，用户进行猜测，直到猜中为止。
# 如果猜中，输出：恭喜你猜中了，数字是 xx。
# 如果猜的数字大，输出：猜测的数字太大了，继续加油
# 如果猜测的数字小，输出：猜测的数字有点小，再来一次
# num = random.randint(1,100)#电脑随机生成一个1到100的数字
# while 1==1:
#     num1 = int(input("请输入你输入的数字："))
#     if num1 < num :
#         print("你所输入的数字有点小哦！请重新输入吧！")
#         continue
#     elif num1 > num :
#         print("你所输入的数字有点大了哦！请重新输入吧！")
#         continue
#     elif num1 == num :
#         print("恭喜你！你猜中了！就是它！")
#         break


# 猜数字游戏：电脑产生（1-100）的随机数，用户进行猜测。
# 如果猜中，输出：恭喜你猜中了，数字是 xx，猜测了xx次。
# 如果猜的数字大，输出：猜测的数字太大了，继续加油
# 如果猜测的数字小，输出：猜测的数字有点小，再来一次
# 如果猜测5 次，还没有猜测出来，输出：太弱了,测试5次还没猜出来,不和你玩了
# num = random.randint(1,100)
# count = 0  # 用于记录输入多少次
# while 1==1 :
#     num1 = int(input("请输入一个数字:"))
#     count += 1
#     if count == 5:
#         print("太弱了！测试了5次还没猜出来，不和你玩了")
#         break
#     if num1 > num :
#         print("你输入的数字有点大哦！请重新输入吧！")
#         continue
#     elif num1 < num :
#         print("你输入的数字有点小哦！请重新输入吧！")
#         continue
#     elif num1 == num :
#         print("恭喜你！输对啦！就是它！")
#         print(count)
#         break


# 要求用户输入一个字符串，遍历当前字符串并打印，如果遇见“q”,则跳出循环。如果遇见“ ”（空格）则跳过当前输出
# word = input("请输入一个字符串：")
# for x in word :
#     if x == "q" :
#         break
#     elif x == " " :
#         continue
#     print(x)


# 使用for循环计算1 - 100 之间的累加和。
# sum = 0
# for x in range(1,101) :
#     sum += x
# print(sum)


# 鲁迅说："我没有说过这句话"。
# s = '鲁迅说："我没有说过这句话"。'
# print(s)


# 做一个简单的用户信息管理系统：
# 提示用户依次输入姓名，年龄和爱好。并且在输入完成之后，一次性将用户输入的数据展示出来。
# names = input("请输入你的姓名：")
# ages = int(input("请输入你的年龄："))
# hobbys = input("请输入你的爱好：")
# print(f"你的姓名是：{names}，年龄是：{ages}，爱好是：{hobbys}")


# 判断单词great是否在字符串words中，如果在，则将每一个great后面加一个s， 如果不在则输出 great不在该字符串中。
# 将整个字符串的每一个单词都变成小写，并使每一个单词的首字母变成大写。
# 去除首尾的空白，并输出处理过后的字符串。
# words = " great craTes Create great craters, But great craters Create great craters "
# print("great" in words)  # 判断单词great是否在字符串words中
# print(words.replace("great", "greats"))  # 将每一个great后面加一个s
# print(words.lower())  # 将整个字符串的每一个单词都变成小写
# print(words.title())  # 并使每一个单词的首字母变成大写。
# print(words.strip())  # 去除首尾的空白


# 有一个列表，判断列表中的每一个元素是否以s或e结尾，如果是，则将其放入一个新的列表中，最后输出这个新的列表。
# list = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
# lista = []
# for x in list:
#     if x[len(x)-1] == "s" or x[len(x)-1] == "e":
#         lista.append(x)
#         print(lista)


# 给定一个列表，首先删除以s开头的元素，删除后，修改第一个元素为"joke"，并且把最后一个元素复制一份，放在joke的后边。
# my_list = ["spring", "look", "strange", "curious", "black", "hope"]
# for x in my_list :
#     if x[0] == "s":
#         my_list.remove(x)
# print(my_list)
# my_list[0] = "joke"
# print(my_list)
# s = my_list[-1]
# my_list.insert(1,s)
# print(my_list)


# 将下列两个列表合并，将合并后的列表去重，之后降序并输出。
# list1 = [11,  4, 45, 34, 51, 90]
# list2 = [4, 16, 23, 51, 0]
# list = list1 + list2
# print(list)
# print(set(list))
# word = set(list)
# a = sorted(word,reverse=True)
# print(a)


# 字典
# my_dict = {"name" : "isaac", "age" : 18, "pi" : 3.14}
# print(my_dict["age"])
# print(len(my_dict))
# my_dict["age"] = 19
# print(my_dict)
# my_dict["gender"] = "男"
# print(my_dict)
# del my_dict["pi"]
# print(my_dict)
# my_dict.clear()
# print(my_dict)


# dict1 = {"name" : "chuanzhi", "age" : 18}
# for key in dict1.keys():
#     print(key)
# for value in dict1.values():
#     print(value)
# for key,value in dict1.items():
#     print(key,":",value)


# product = [{"name":"电脑","price": 7000, "name": "鼠标", "price": 30,"name": "usb电动小风扇", "price": 20,"name": "遮阳伞",
#            "price": 50}]
# money = 8000
# sum = 0
# for x in product:
#     sum += x["price"]
# if money >= sum:
#     print("你可以买他们！")
# else :
#     print("你买不起他们！")

#
# def num(**kwargs):
#     for key, value in kwargs.items():
#         print("key:", key, "value:", value)
#
#
# num(name="电脑", price=700)


# dict = {'老大':'15岁',
#         '老二':'14岁',
#         '老三':'2岁',
#         }
# print(dict.items())
# for key,values in dict.items():
#     print(key + '已经' + values + '了')
# import os
#
# stu_list = []
#
#
# def main():
#     print("1.添加学生 ")
#     print("2.删除学生 ")
#     print("3.修改学生信息 ")
#     print("4.查询单个学生信息 ")
#     print("5.查询所有学生信息 ")
#     print("6.退出系统 ")
#
#
# def load() :
#     global stu_list
#     if os.path.exists('student.txt'):
#         f = open("student.text","r",encoding="utf-8")
#         buf = f.read()
#         if buf :
#             stu_list = eval(buf)
#         f.close()
#
#
# def save() :
#     f = open("student.text","w",encoding="utf-8")
#     f.write(str(stu_list))
#     f.close()
#     os.chdir('../')
#
#
# def information():
#     name = input("请输入学生的姓名:")
#     for stu in stu_list:
#         if name == stu["name"]:
#             print("-------------不添加-------------")
#             return
#     age = input("请输入学生的年龄:")
#     gender = input("请输入学生的性别:")
#     stu_dict = {"name": name, "age": int(age), "gender": gender}
#     stu_list.append(stu_dict)
#     print(stu_list)
#     print("==================学生信息添加成功==================")
#
#
# def hello():
#     name = input("请输入学生的姓名:")
#     for stu in stu_list:
#         if name == stu["name"]:
#             stu_list.remove(stu)
#             print("==========该学生信息已被删除！============")
#             return
#     else:
#         print("==================无该生信息！==================")
#
#
# def change():
#     name = input("请输入学生的姓名:")
#     stu: object
#     for stu in stu_list:
#         if name == stu["name"]:
#             while 2 == 2:
#                 choice = int(input("请选择你要修改的内容（1.姓名 2.年龄 3.性别）:"))
#                 if choice == 1:
#                     names = input("请输入你修改后学生的名字:")
#                     stu["name"] == names
#                     y = int(input("你是否还要修改信息（1.需要 2.不需要）："))
#                     if y == 1:
#                         continue
#                     else:
#                         break
#                 elif choice == 2:
#                     ages = input("请输入你修改后学生的年龄:")
#                     stu["age"] == ages
#                     y = int(input("你是否还要修改信息（1.需要 2.不需要）："))
#                     if y == 1:
#                         continue
#                     else:
#                         break
#                 elif choice == 3:
#                     genders = input("请输入你修改后学生的年龄:")
#                     stu["gender"] == genders
#                     y = int(input("你是否还要修改信息（1.需要 2.不需要）："))
#                     if y == 1:
#                         continue
#                     else:
#                         break
#                 else:
#                     print("你输入的无效，请重新输入！")
#                     continue
#
#
# def one():
#     name = input("请输入学生的姓名:")
#     for stu in stu_list:
#         if name == stu["name"]:
#             print("这名学生的信息是：",stu)
#             return
#
#
# def suoyou():
#     if len(stu_list) > 0 :
#         for student in stu_list :
#             print(student)
#
#
# def zhu() :
#     load()
#     while 1 == 1:
#         main()
#         num = int(input("去请选择要进行的操作编号："))
#         if num == 1:
#             print("添加学生")
#             information()
#         elif num == 2:
#             print("删除学生")
#             hello()
#         elif num == 3:
#             print("修改学生信息")
#             change()
#         elif num == 4:
#             print("查询单个学生信息")
#             one()
#         elif num == 5:
#             print("查询所有学生信息")
#             suoyou()
#         elif num == 6:
#             print("退出系统")
#             save()
#             zhu()
#         else:
#             print("输入有误！请重新输入！")
#             continue
#
#
# zhu()


# class Dog(object):
#     def __init__(self):
#         self.name = None
#
#     def play(self):
#         print(f"我是狗！{self.name}")
#         print(F"我也是狗！{self.age}")
#
#
# dog = Dog()
# dog.name = "大黄"
# dog.age = 19
# dog.play()
# dog1 = Dog()
# dog1.name = "大黑"
# dog1.age = 18
# dog1.play()


# class Potato(object):
#     def __init__(self):
#         self.name_list = []
#         self.status = "生的"
#         self.total_time = 0
#
#     def cook(self, time):
#         self.total_time += time
#         if self.total_time < 3:
#             self.status = "生的"
#         elif self.total_time < 6:
#             self.status = "半生不熟的"
#         elif self.total_time < 8:
#             self.status = "熟的"
#         else:
#             self.status = "糊了"
#
#     def __str__(self):
#         buf = ",".join(self.name_list)  # 让列表的中括号消失
#         if len(self.name_list) > 0:
#             return f"地瓜的状态是{self.status},烤了{self.total_time}分钟！用了{buf}调料"
#         else:
#             return f"地瓜的状态是{self.status},烤了{self.total_time}分钟！没有使用调料"
#
#     def add(self, name):
#         self.name_list.append(name)
#
#
# potato = Potato()
# potato.cook(7)
# potato.add("孜然")
# print(potato)


# class Furniture(object):
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
#
#     def __str__(self):
#         return f"家具的类型是<{self.name}>,占地{self.area}平方米"
#
#
# class House(object):
#     def __init__(self, address, area, ):
#         self.address = address
#         self.H_area = area
#         self.obj_Furniture_List = []
#         self.free_area = area
#
#     def add_furniture(self, obj_Furniture):
#         if self.free_area > obj_Furniture.area:
#             self.free_area -= obj_Furniture.area
#             self.obj_Furniture_List.append(obj_Furniture.name)
#             print("添加成功！")
#         else:
#             print("添加失败！")
#
#     def __str__(self):
#         if len(self.obj_Furniture_List) > 0:
#             buf = ",".join(self.obj_Furniture_List)
#             return f"房子的地址是《{self.address}》,占地面积是《{self.H_area}》,剩余面积是《{self.free_area}》,家具有{buf}"
#         else:
#             print("你还没有添加家具！")
#
#
# bed = Furniture("床", 15)
# room = Furniture("房间", 50)
# print(bed)
# house = House("中国广州", 100)
# house.add_furniture(bed)
# house.add_furniture(room)
# print(house)


# # 1.定义Dog类
# class Dog(object):
#     def __init__(self, name):
#         # 添加属性
#         self.age = 0
#         self.name = name
#
#     def __str__(self):
#         return f'名字：{self.name}, 年龄：{self.age}。'
#
#
# # 2.定义XTQ类继承Dog类
# class XTQ(Dog):
#     # 子类重写了父类的__init__()方法,默认不再调用父类的__init__()方法, 需要手动地调用父类的__init__()方法
#     # 注意：子类init方法的形参，一般都先写父类的形参，再写子类自己独有的形参。
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color
#
#     def __str__(self):
#         return f'名字：{self.name}；年龄：{self.age}；毛色：{self.color}。'
#
#
# # 3.创建XTQ类对象
# xtq = XTQ('小黑', '红色')
# print(xtq)  # 名字：小黑；年龄：0；毛色：红色。

/
# class Dog(object):
#     def born(self):
#         """生小狗的方法,生一个小狗,休息30天"""
#         print('生了一只小狗...')
#         self.__sleep()
#
#     def __sleep(self):
#         print('休息30天~')
#
#
# dog = Dog()
# # dog.__sleep()  # 报错
# dog.born()
