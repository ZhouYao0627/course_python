class Animal():

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def run(self):
        print('动物会跑')

    def sleep(self):
        print('动物睡觉')

# 父类中的所有方法都会被子类继承，包括特殊方法，也可以重写特殊方法
class Dog(Animal):

    def __init__(self, name, age):
        # super可以获取当前类的父类
        # 并且通过super()返回对象调用方法时，不需要传递self
        super.__init__(name)
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def bark(self):
        print('汪汪汪')

    def run(self):
        print('狗跑···')


d = Dog('旺财',3)
d.name = '小黑'
print(d.name, d.age)

