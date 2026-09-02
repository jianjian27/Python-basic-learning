#input语句（函数）：获取键盘输入的数据,获取的数据都会视为字符串类型
#s = input(提示信息)

name = input("请输入你的名字")
print(f"hello,{name}")

input("请输入密码")
m = input("请输入取款金额")
#后续运算，m需要转为int类型，使用int（）
total = 10000
remain = total - int(m)
print(remain)
print(f"余额为:{total - int(m)}")