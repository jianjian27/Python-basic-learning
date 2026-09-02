# 实例属性：实例属性属于每个对象，通常在类的构造方法中定义。每个对象都有自己独立的实例属性，它们的值可以不同。实例属性通常用于存储对象的状态信息。
# 类属性：类属性属于整个类，而不是单个对象。它在类定义时创建，并且所有实例共享同一个类属性。类属性通常用于存储类的公共信息或默认值。

class Car:
    # 类属性（所有实例对象共享的）
    wheel = 4      # 轮胎数量
    tax_rate = 0.1 # 购置税税率

    def __init__(self, c_color, c_brand, c_name, c_price):
        # 实例属性
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price

    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶中....")

    def total_cost(self, discount, rate=0.1):
        total_cost = self.price * discount + rate * self.price
        return total_cost