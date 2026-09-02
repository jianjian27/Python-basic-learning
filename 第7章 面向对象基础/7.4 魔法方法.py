# 魔法方法：是指Python中提供的以双下划线开头和结尾的特殊方法，用于定义类的特殊行为，比如：__init__
# 魔法方法不需要手动调用，Python会在合适的时机自动调用
# __init__
# __str__
# __eq__
# __lt__,__le__,__gt__,__ge__

class Car:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
# 定义实例方法
    def running(self):
        print(f"{self.brand}{self.name}正在行驶 ")
# 定义魔法方法
    def __str__(self):
        return f"{self.color} {self.brand} {self.name}"
    def __eq__(self, other):
        return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price
    def __lt__(self, other):
        return self.price < other.price


