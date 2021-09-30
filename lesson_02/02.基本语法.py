# name = '孙悟空'
#
# print('欢迎'+name+'光临') # 拼串
# print('欢迎',name,'光临')# 多个参数
# print('欢迎 %s 光临'%name)
# print(f'欢迎{name}光临')

# num = 18

# if num > 10 and num < 20:
#     print('num比10大，num比20小')

# if 10 < num < 20:
#     print('num比10大，num比20小')

# s = input('请输入任意内容：')
# print('用户输入的内容是：',s)

# username = input('请输入您的用户名：')
# if username == 'admin':
#     print(username,'欢迎您')
# else:print('很抱歉，您不是管理员')

# age = input('请输入您的年龄：')
# age = int(age)
# if age >= 18:
#     print('女子得体，落落大方')
# else:print('邻家有女初长成')

# i = 0
# while i < 10:
#     print(i,'hello')
#     i += 1
# else:print('else中的代码块')

# 求100以内所有奇数的和
# i = 1
# sum = 0
# while i <= 100:
#     if i % 2 != 0 :
#         sum += i
#     i += 1
# print(sum)

# 求100以内所有7的倍数之和，以及个数
# i = 1
# sum = 0
# count = 0
# while i < 100:
#     if i % 7 == 0:
#         count += 1
#         sum += i
#     i += 1
# print('100以内所有7的倍数之和为:',sum)
# print('个数为:',count)

# 水仙花数
# i = 100
# while i < 1000:
#     z = i // 100  # 百位数
#     y = (i - z * 100) // 10 # 十位数
#     x = i % 10  # 个位数
#     if x**3 + y**3 + z**3 == i:
#         print(i)
#     i += 1

# 质数
# num = int(input('请输入您的数：'))
# i = 2
# flag = 1 # 表示是质数
# while i < num:
#     if num % i == 0:
#         flag = 0 # 不是质数
#     i += 1
#
# if flag == 0:
#     print(num,'不是质数')
# else:print(num,'是质数')

# # 创建一个循环来控制图形的高度
# i = 0
# while i < 5:
#     j = 0
#     # 创建一个循环来控制图形的宽度
#     while j < 5:
#         print('*',end='')
#         j += 1
#     print()
#     i += 1

# 打印一个三角形
# i = 0
# while i <= 5:
#     print('*' * (i + 1))
#     i += 1

# 打印一个三角形
# i = 0
# while i < 5:
#     j = 0
#     while j <= i:
#         print('*',end='')
#         j += 1
#     print()
#     i += 1

# i = 5
# while  0 < i <= 5:
#     j = 0
#     while j < i:
#         print('*',end='')
#         j += 1
#     print()
#     i -= 1












