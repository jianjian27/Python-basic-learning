# 多态：同一个接口，不同的实现。在Python中，多态通常通过继承和方法重写来实现。

class Animal:

    def speak(self):
        print("动物发出声音")


class Dog(Animal):

    def speak(self):
        print("小狗：汪汪汪")


class Cat(Animal):

    def speak(self):
        print("小猫：喵喵喵")


class Duck(Animal):

    def speak(self):
        print("鸭子：嘎嘎嘎")


# 多态函数
def make_sound(animal):
    animal.speak()


if __name__ == "__main__":

    dog = Dog()
    cat = Cat()
    duck = Duck()

    make_sound(dog)
    make_sound(cat)
    make_sound(duck)