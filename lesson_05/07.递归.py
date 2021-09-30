# 求任意数的阶乘

# n = 10
# # result = 1
# for i in range(1,10):
#      n *= i
# print(n)


# def factorial(n):
#     result = n
#     for i in range(1,n):
#         result *= i
#     return result
#
# print(factorial(10))

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(10))

# 求n的i次幂
# def power(n, i):
#     if i == 1:
#         return n
#     else:
#         return n * power(n, i - 1)
#
# print(power(4,3))

# 求回文数
def hui_wen(s):
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return hui_wen((s[1:-1]))

print(hui_wen('aba'))












