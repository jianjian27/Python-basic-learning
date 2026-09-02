# 类的定义
#
# 定义类
# class 类名
#     结构
#
# 创建对象
# 对象名 = 类名()
# 对象名.属性名1 = 属性值1
# 对象名.属性名2 = 属性值2

# class Car: #类名的命名规范，遵循驼峰命名法，每个单词首字母都大写，单词之间没有分隔符
#     pass
# c1 = Car()
# c1.brand = "BMW" # 动态添加属性
# c1.name = "X5"
# c1.price = 500000
# print(c1.__dict__) #__dict__是Python中用户自定义类实例的一个特殊属性，以字典形式存储对象的属性
# print(c1)

# 定义在类的外面的称之为函数，定义在类中的函数称之为方法
# class 类名：
#     def __init__(self,参数列表):
#         self.属性名 = 参数值
#         self.属性名 = 参数值
# 对象名 = 类名(参数列表)

class Car:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car类型的对象初始化完毕，对象属性已经添加完毕")

c1 = Car("red","BMW","X7",800000)
print(c1.__dict__)

c2 = Car("blue","奔驰","E300",450000)
print(c2.__dict__)