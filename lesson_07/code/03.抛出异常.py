# 也可以自定义异常类，只需要创建一个类继承Exception即可
class MyError(Exception):
    pass

def add(a, b):
    # 如果a和b中有负数，就向调用处抛出异常
    if a < 0 or b < 0:
        # raise用于向外部抛出异常，后边可以跟一个异常类，或异常类的实例
        # raise Exception('两个参数中不能有负数')
        raise MyError('自定义的异常')
    r = a + b
    return r

print(add(-123, 456))
