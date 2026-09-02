# 匿名函数：没有名称的函数，需要通过lambda表达式来声明函数，可以简化简单函数的编写(单行表达式)
# lambda 参数列表 : 函数体
lambda : print("Hello World")
lambda x,y: x+y

# 调用需要赋值给一个变量
str1 = lambda:print("Hello World")
add = lambda a,b: a+b
print(add(10,20))

# 函数逻辑比较简单（单行表达式）且只在一个地方使用时，可以考虑使用匿名函数，简化书写（通常作为高阶函数的参数使用）
# 匿名函数中可以返回结果，也可以不返回结果。返回结果时，不需要写return，表达式的运行结果就是要返回的结果

data_list = ["c++","c","python","jack","php","java","go","javascript","rust"]
data_list.sort()# 默认按字母排序
print(data_list)
data_list.sort(key = lambda item : len(item))
print(data_list)