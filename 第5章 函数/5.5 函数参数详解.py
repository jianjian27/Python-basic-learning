# 传参方式指的是，在调用函数时，传递实参的方式
# 1.位置参数：调用函数时根据函数定义时的位置来传递参数，需要顺序一致
# 2.关键字参数：调用函数时以函数定义时形参名称作为关键字，以“键=值”的形式来传递参数，不要求顺序
# 如果位置参数与关键字参数混用，关键字参数必须在位置参数之后
from unittest import result


# 默认参数：也称缺省参数，用于在定义函数时，为参数提供默认值，调用函数时，可以不传递有默认值的参数
def reg_stu(name,age,gender,city = 'Beijing'):
    print(f"name:{name},age:{age},gender:{gender},city:{city}")
    return {"name":age,"gender":gender,"city":city}
stu = reg_stu("czr",18,"man")
print(stu)
# 默认参数必须放在没有默认值的参数列表后面，一个函数在定义时可以设置多个默认参数
# 函数调用时，如果为默认参数传递了值，则会修改默认的参数值；如果没有传递该参数，则直接使用默认值

# 不定长参数：也叫可变参数，用于函数定义及调用时参数个数不确定的场景
# 位置传递，关键字传递
# def calc_data(*args):   位置传递,将多个参数封装进一个元组
def calc_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)
    return min_data,max_data,round(avg_data,1)# round 四舍五入函数
calc_data(1,2,3,4,5)
print(calc_data(1,2,3,4,5))

# def cal_data(**kwargs):   关键字传递，将多个参数封装进一个字典
def calc_data(*args,**kwargs):
    """
    根据传入的这批数据，计算最小值，最大值，平均值
    :param args:不定长位置参数
    :param kwargs:不定长关键字参数
        round: 不保留的小数位个数
        print: 是否打印输出
    :return:最小值，最大值，平均值
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)
    print(kwargs)

    if kwargs.get("round") is not None:
        avg_data = round(avg_data,kwargs.get("round"))

    if kwargs.get("print"):
        print(min_data,max_data,avg_data)

    return min_data,max_data,avg_data
print(calc_data(1,2,3,4,5,round=3,print=True))

# 参数类型
# 普通参数：数字，布尔，字符串，列表，元组，集合，字典等
# 特殊参数：函数
def add (x,y):
    return x+y

def calc(x,y,oper):
    return oper(x,y)
result = calc(10,20,add)
print(result)