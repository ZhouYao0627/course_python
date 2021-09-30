a = 10
b = 20

# 添加了_的变量，只能在模块内部访问，在通过import *引入时，不会引入_开头的变量
_c = 30


def test():
    print('test')


def test2():
    print('test2')


class Person():
    def __init__(self):
        self.name = 'swk'


#  编写测试代码，这部分代码，只有当当前模块为主模块的时候才需要执行
#  而当模块被其它模块引入时，不需要执行的，此时我们就需要检查当前模块是否为主模块
if __name__ == '__main__':
    test()
    test2()
    p = Person()
    print(p.name)
