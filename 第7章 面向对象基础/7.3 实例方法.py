# 在类中定义实例方法时，定义语法与之前学习的函数定义方式是一致的
# class 类名：
#     def __init__(self,参数列表):
#         self.属性名 = 参数值
#         self.属性名 = 参数值
#     def 方法名(self,形参列表)：
#       ...
#     def 方法名(self,形参列表)：
#       ...
class Car:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
    # 定义实例方法
    def running(self):
        print(f"{self.brand}{self.name}正在行驶 ")

    def total_cost(self, discount, rate):
        """
        计算车的总费用，包含价格和税费
        :param discount: 折扣
        :param rate: 税率
        :return: 总费用
        """
        total_cost = rate * self.price + self.price * discount
        return total_cost

c1 = Car("red","BMW","X7",800000)

c1.running()
total = c1.total_cost(0.9, 0.1)
print("总费用",total)