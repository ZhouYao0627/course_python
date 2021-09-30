l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 检查数字是否为偶数
def fn2(i):
    if i % 2 == 0:
        return True
    else:
        return False


# 检查数字是否大于5
def fn3(i):
    if i > 5:
        return True
    else:
        return False


# 取出3的倍数
# def fn4(i):
#     if i % 3 == 0:
#         return True
#     else:
#         return False

def fn4(i):
    return i % 3 == 0


def fn(func, lst):
    new_list = []
    for n in lst:
        if func(n):
            new_list.append(n)

    return new_list

# print(fn(fn3, l))

r = filter(lambda i : i % 3 == 0, l)
print(list(r))

# def fn5(a , b):
#     return a + b

# (lambda a,b : a + b)(10,20)

l = ['bb','aaaa','c','ddddddd','fff']

l.sort(key=len)
print(l)










