# 2-16 集合（set）无序不重复
# 用处：去除重复值，进行数学集合运算
# 特性：无序；元素不重复（有重复的元素只会打印出一个元素）；集合本质上是只有键的字典
# seta={1,35,153,13,165,1561,1,651,547,"hallo"}
# print(seta)

# 去重
lista = [1, 1, 2, 51, 316551, 165, 1, 0, 1, 651, 20]
seta = {1, 35, 153, 13, 165, 1561, 1, 651, 547, "hallo"}
n = set(lista)  # set是将其他序列转换为set
listb = list(seta)  # 将其他序列抓换为list
print(n)
print(listb)

# 集合运算
# seta={1,15,15,154,13,6,59,594}
# setb={854,489,4624,1,14,612,591,5,15}
# print(seta&setb)#获取交集
# print(seta|setb)#获取并集
# print(seta-setb)#获取差集（在seta中有但在setb中没有的）
