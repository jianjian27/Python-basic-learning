# append()
# insert()
# remove()
# pop()
# sort()
# reverse()

# s = [54,15,75,108,23,78,75]
# s.sort()
# print(s)
#
# a = []
# m = 0
# for i in range(3):
#     a.append(int(input("请输入：")))
#     m = m + a[i]
# print(a)
# a.sort()
# print(a)
# print(f"min{a[0]},max{a[-1]},average{m/3}")
# n = sum(a)#sum()求和
# print(n)
# l = len(a)#len()获取元素个数
# print(l)

s1 = [19,3,54,64,875,20,109,232,123,54]
s2 = [55,80,72,35,60,123,54,29,91]
for i in s2:
    if i in s1:
        continue
    else:
        s1.append(i)
print(s1)

#解包操作：将列表这一类容器解开成一个一个独立的元素
s3 = [*s1,*s2]
print(s3)
#组包

# “+” 号可以直接合并
s4 = s1 + s2
print(s4)

# 列表推导式：按照一定的规则快速生成一个列表
#[要插入的值 for i in 序列/列表]
s5 = [i**2 for i in range(1,21)]
print(s5)

s6 = [12,32,45,77,80,92,33,57,97,98]
s7 = [i**2 for i in s6 if i%2 == 0]
#列表推导式：后面可进行条件判断
print(s7)