class A(object):
    def test(self):
        print('AAA')

class B(object):
    def test(self):
        print('BBB')

# 在Python中是支持多重继承的，也就是可以为一个类同时指定多个父类，并且会获取到所有父类中的方法
# 如果多个父类中有同名的方法，则会先在第一个父类中寻找，然后找第二个，然后找第三个
# 前边父类的方法会覆盖后边父类的方法

class C(A, B):
    pass

# print(C.__bases__) # (<class '__main__.A'>,)
# print(C.__bases__) # (<class '__main__.B'>,)
# print(C.__bases__) # (<class '__main__.A'>, <class '__main__.B'>)

c = C()
c.test()
# c.test2()









