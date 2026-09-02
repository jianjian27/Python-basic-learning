# 多继承：一个类可以同时继承多个父类的属性和方法。在多继承中，子类可以访问所有父类的公有属性和方法。
# mro：方法解析顺序（Method Resolution Order），用于确定在多继承情况下方法的调用顺序。

class Car:
    """汽车类"""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def run(self):
        print(f"{self.brand} {self.model} 正在行驶...")


class Electric:
    """电动车功能"""

    def charge(self):
        print("正在充电...")

    def battery_info(self):
        print("当前电池容量：100 kWh")


class AutonomousDriving:
    """自动驾驶功能"""

    def auto_drive(self):
        print("自动驾驶已开启...")

    def park(self):
        print("自动泊车中...")


# 同时继承三个类
class SmartCar(Car, Electric, AutonomousDriving):

    def __init__(self, brand, model):
        # 调用父类Car的构造函数
        super().__init__(brand, model)

    def introduce(self):
        print(f"我是 {self.brand} {self.model}")


if __name__ == "__main__":

    car = SmartCar("小米", "SU7")

    car.introduce()

    # 来自 Car
    car.run()

    # 来自 Electric
    car.charge()
    car.battery_info()

    # 来自 AutonomousDriving
    car.auto_drive()
    car.park()

    # 查看方法解析顺序
    print(SmartCar.__mro__)