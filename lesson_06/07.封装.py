class Person():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property  # 使用property装饰的方法，必须和属性名是一样的
    def name(self):
        print('get方法执行了')
        return self._name

    @name.setter  # setter方法的装饰器：@属性名.setter
    def name(self, name):
        print('setter方法执行了')
        self._name = name

    @property  # 使用property装饰的方法，必须和属性名是一样的
    def age(self):
        # print('get方法执行了')
        return self._age

    @age.setter  # setter方法的装饰器：@属性名.setter
    def age(self, age):
        # print('setter方法执行了')
        self._age = age


p = Person('周', 24)

p.name = '111'
p.age = 22

print(p.name, p.age)
