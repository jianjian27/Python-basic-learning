# 封装：将数据和操作数据的方法组合在一起，形成一个独立的单元（类），并对类的内部实现细节进行隐藏，只暴露必要的接口给外部使用。
# 私有：在Python中，可以通过在属性或方法名前加上双下划线（__）来表示私有。私有属性和方法只能在类的内部访问，不能从类的外部直接访问。
# 公共：在Python中，公共属性和方法是可以在类的外部访问的。公共属性和方法不需要加下划线前缀，可以直接通过类的实例进行访问。
# Python中没有真正的私有属性和方法，但通过命名约定（如双下划线前缀）可以实现一定程度的封装和隐藏。

class Car:

    def __init__(self, brand, model, color, owner):
        self.brand = brand          # 品牌(公有属性)
        self.model = model          # 型号(公有属性)
        self.color = color          # 颜色(公有属性)

        self.__owner = owner        # 拥有者(私有属性)

    def start(self):  # 启动
        print(f'{self.brand} {self.model} 正在启动...')

    def run(self):  # 行驶
        print(f'{self.__owner}：{self.brand} {self.model} 正在行驶...')
        self.__control_fuel()

    def stop(self):  # 停止
        print(f'{self.brand} {self.model} 停止行驶...')

    def __control_fuel(self):  # 私有方法
        print(f'{self.brand} {self.model} 正在控制油门...')

    def get_owner(self):
        return self.__owner[0:1] + "**"


if __name__ == '__main__':

    car = Car(
        brand='Audi',
        model='A6',
        color='黑色',
        owner='jianjian'
    )

    print(car.brand)
    print(car.model)
    print(car.color)

    # print(car.__owner)

    car.start()
    car.run()
    car.stop()

    # car.__control_fuel()

    print(car.get_owner())