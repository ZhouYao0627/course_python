class Animal():
    def run(self):
        print('动物会跑')

    def sleep(self):
        print('动物睡觉')

class Dog(Animal):
    def bark(self):
        print('汪汪汪')

    def run(self):
        print('狗跑···')

# class hashiqi():
#     def fan_sha(self):
#         print('我是一只傻傻的哈士奇')

d = Dog()
d.run()
# d.sleep()
# d.bark()


