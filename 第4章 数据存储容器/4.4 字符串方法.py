# find()查找子串，返回第一次出现的索引位置，找不到返回-1
# count()统计子串在字符串中出现的次数
# upper()转大写，不改变字符串本身
# lower()转小写，不改变字符串本身
# split()将字符串按指定分隔符分割成列表
# strip()去除字符串两端的空白字符或指定字符
# replace()将字符串中的指定子串替换为新的子串
# startswith()检查字符串是否以指定子串开头，返回布尔值
# s = "hello-czr-20260821"
# a = s.count("czr")
# print(a)
# s1 = s.split("-")
# print(s1)
# s2 = s.replace("-", "")
# print(s2)
# s3 = s.upper()
# print(s3)
# print(s)

admin = input("email:")
l1 = admin.count("@")
l2 = admin.find(".")
if l1 != 1 or l2 == -1:
	print("wrong email")
else:
    print("right email")