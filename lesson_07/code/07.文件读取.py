# import pprint

file_name = 'demo2 .txt'

# try:
#     with open(file_name) as file_obj:
#         print(file_obj.read())
# except FileNotFoundError:
#     print(r'{file_name} 文件不存在')


with open(file_name,encoding='utf-8') as file_obj:
    # readline()
    # 该方法可以用来读取一行内容
    # print(file_obj.readline())

    # readlines()
    # 该方法用于一行一行的读取内容，它会一次性的将读取到的内容封装到一个列表当中
    # r = file_obj.readlines()
    data = file_obj.read().splitlines()
    print(data)

    # for t in file_obj:
    #     print(t,end='')


