# 求任意三个数的乘积
# def fn(a,b,c):
#     print(a,"*",b,"*",c,"=",a*b*c)
#
# fn(1,2,3)

# 显示不同的欢迎信息
# def fn2(username):
#     print('欢迎',username,'光临')
# fn2('x')

def fn(a=5, b=10, c=20):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)

def fn2(a):
    print('a = ', a)
    a(1, 2, 3)

fn2(fn)

# 位置参数
# fn(1, 2, 3)

# 关键字参数
# fn(b=1, c=2, a=3)

# 位置参数和关键字参数混合使用
# fn(1, c = 30)

# def fn4(a):
#     a[0] = 30
#     print('a = ', a, id(a))
#
# c = [1, 2, 3]

# fn4(c)
# 浅复制
# fn4(c.copy())

# print('c = ', c, id(c))
