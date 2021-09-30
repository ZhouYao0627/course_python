from time import *

begin = time()

# i = 2
# while i <= 10000:
#     flag = 1
#     j = 2
#     while j < i:
#         if i % j == 0:
#             flag = 0
#         j += 1
#     if flag == 1:
#         # print(i)
#         pass
#     i += 1

# 第一次优化
# i = 2
# while i <= 10000:
#     flag = 1
#     j = 2
#     while j < i:
#         if i % j == 0:
#             flag = 0
#             break
#         j += 1
#     if flag == 1:
#         # print(i)
#         pass
#     i += 1

# 第二次优化
i = 2
while i <= 10000:
    flag = 1
    j = 2
    while j <= i ** 0.5:
        if i % j == 0:
            flag = 0
            break
        j += 1
    if flag == 1:
        # print(i)
        pass
    i += 1

end = time()

print('程序执行花费了:', end - begin, '秒')


# 未优化前，10000个数执行花费了: 9.64079999923706 秒
# 第一次优化后，10000个数执行花费了: 1.1856000423431396 秒
# 第二次优化后，10000个数执行花费了: 0.062399864196777344 秒

