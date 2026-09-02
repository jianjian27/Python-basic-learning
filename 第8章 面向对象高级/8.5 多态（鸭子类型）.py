# 鸭子类型：如果一个对象实现了某个接口的所有方法，那么它就可以被当作该接口的实例来使用，即使它不是该接口的直接子类。这种类型检查是在运行时进行的，因此也被称为“动态类型”或“结构化类型”。

class Dog:

    def speak(self):
        print("小狗：汪汪汪")


class Cat:

    def speak(self):
        print("小猫：喵喵喵")


class Robot:

    def speak(self):
        print("机器人：你好，人类！")


def make_sound(obj):
    obj.speak()


if __name__ == "__main__":

    dog = Dog()
    cat = Cat()
    robot = Robot()

    make_sound(dog)
    make_sound(cat)
    make_sound(robot)