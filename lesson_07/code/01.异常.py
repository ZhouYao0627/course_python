#处理异常
# 将可能出错的代码放到try语句中，
# 若代码没有错误，则会正常执行，若出错则执行except子句中的代码

# try 语句：try语句是必须的，else语句有没有都行，except和finally至少有一个
# try:
#     代码块(可能出现的错误)
# except 异常类型 as 异常名:
#     代码块(出现错误以后的处理方式)
# except 异常类型 as 异常名:
#     代码块(出现错误以后的处理方式)
# except 异常类型 as 异常名:
#     代码块(出现错误以后的处理方式)
# else:
#     代码块(没出错时要执行的语句)
# finally:
#     代码块(该代码块总会执行)


print('hello')
try:
    print(10/0)
except:
    print('hhh')
else:
    print('程序正常执行，没有错误')
print('你好')









