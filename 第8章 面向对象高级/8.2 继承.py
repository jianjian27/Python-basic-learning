# 继承：一个类可以继承另一个类的属性和方法(包括公有和私有)，被继承的类称为父类或基类，继承的类称为子类或派生类。子类可以使用父类的属性和方法，也可以定义自己的属性和方法。

class Car:
    """父类（基类）"""

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def start(self):
        print(f"{self.brand} {self.model} 正在启动...")

    def run(self):
        print(f"{self.brand} {self.model} 正在行驶...")

    def stop(self):
        print(f"{self.brand} {self.model} 已停止。")


class ElectricCar(Car):
    """子类（派生类）"""

    def __init__(self, brand, model, color, battery):
        # 调用父类的构造函数
        super().__init__(brand, model, color)

        # 子类新增属性
        self.battery = battery

    # 子类新增方法
    def charge(self):
        print(f"{self.brand} {self.model} 正在充电...")

    # 重写父类的方法（方法重写）
    def run(self):
        print(f"{self.brand} {self.model} 正在安静地行驶，当前电量：{self.battery}%")



if __name__ == "__main__":

    car = ElectricCar(
        brand="小米",
        model="SU7",
        color="银色",
        battery=95
    )

    print(car.brand)
    print(car.model)
    print(car.color)
    print(car.battery)

    car.start()     # 继承自父类
    car.run()       # 子类重写的方法
    car.charge()    # 子类自己的方法
    car.stop()      # 继承自父类