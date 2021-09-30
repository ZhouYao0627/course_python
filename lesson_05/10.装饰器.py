def add(a, b):
    r = a + b
    return r


def mul(a, b):
    r = a * b
    return r


def fn():
    print('woshifn')


#
# def new_add(a,b):
#     print('函数开始执行···')
#     r = add(a,b)
#     print('函数结束执行···')
#     return r
#
# r = new_add(123,456)
# print(r)

def begin_end(old):
    def new_function(*args, **kwargs):
        print('函数开始执行···')
        result = old(*args, **kwargs)
        print('函数结束执行···')
        return result
    return new_function

# f = begin_end(fn) # f就相当于new_function
# f2 = begin_end(add) # f2就相当于new_function
f3 = begin_end(mul) # f3就相当于new_function

# r = f()
# r = f2(123,456)
# r = f3(123,456)
# print(r)

@begin_end #加了一个装饰器，若是多个则从下向上装饰
def say_hello():
    print('大家好···')

say_hello() # say_hello相当于new_function
