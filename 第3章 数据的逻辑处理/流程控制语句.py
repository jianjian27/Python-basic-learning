# 条件判断if
# 只有在满足指定条件，才会执行对应代码逻辑
# if 要判断的条件：
#     条件成立时，要执行的操作
# 注意缩进格式，缩进正确才是一个代码块
# score = float(input("分数"))
# if score > 700:
#     print("hhh")
from turtledemo.penrose import start

# account = float(input("account:"))
# password = float(input("password:"))
# if account == 18888 and password == 666:
#     print("hello")
# if account != 18888 or password != 666:
#     print("try again")

# if account != 18888 or password != 666:
#     print("try again")
# else:
#     print("hello")

# year = int(input("year:"))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("闰年")
# else:
#     print("平年")
#
# if year > 0:
#     print(f"{year}正")
# elif year < 0:
#     print("负")
# else:
#     print("0")

# 模式匹配 match...case
# day = int(input("day:"))
# match day:
#     case 1|3 if day == 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case _:
#         print("hhh")

# # 循环 while for 嵌套
# while day <= 3:
#     print(f"day:{day}")
#     day += 1
# else:
#     print(f"day:{day}")

# i = 1
# s = 0
# while i <= 100:
#     if i % 2 == 0:
#         s = s + i
#         i = i + 1
#     else:
#         i = i + 1
# print(s)
#
# msg = "everlasting"
# for i in msg:
#     print(i) 自带换行效果

# while循环更关注循环的条件，for循环关注遍历每一个元素

# range语句：生成指定规则的数字序列
# range(end)->从0开始，到end结束，包含0，不包含end
# range(start,end)->从start开始，到end结束，包含start，不包含end
# range(start,end,step)->从start开始，到end结束，步长step，包含start，不包含end
# s = 0
# for i in range(1,100):
#     if i % 2 == 0:
#         continue
#     else:
#         s = s + i
# else:
#     print(s)
#
# s2 = 0
# for i in range(100,501):
#     if i % 3 == 0:
#         s2 = s2 + i
#     else:
#         continue
# else:
#     print(s2)

# m = int(input("long:"))
# n = int(input("wide:"))
# a = 1
# b = 1
# while a <= n:
#     while b < m:
#         print("*",end="1")
#         b = b + 1
#     else:
#         print("*")
#         b = 1
#         a += 1

# for i in range(1,10):
#     m = 1
#     n = i
#     while m <= n:
#         print(f"{m} × {n} = {m*n}",end="\t")
#         m = m + 1
#     print()

# admin1 = "admin"
# admin2 = "czr"
# admin3 = "hh"
# p1 = "666"
# p2 = "777"
# p3 = "hhh"
#
# while True:
#     a1 = input("admin name:")
#     p = input("password:")
#     if a1 == admin1 or a1 == admin2 or a1 == admin3 and a1 != None and p1 != None and p2 != None and p3 != None:
#         if p == p1 or p == p2 or p == p3:
#             print("hello")
#             break
#         else:
#             print("try again")
#     else:
#         print("can't be emperty")

import random
random_num = random.randint(1,100)
while True:
    m = int(input("please input:"))
    if m == random_num:
        print("you are right")
        break
    elif m > random_num:
        print("big")
    elif m < random_num:
        print("small")