file_name = 'demo2 .txt'
try:
    with open(file_name) as file_obj:
        # 如果直接调用read()他会将文本文件的所有内容全部都读出来
        # 对于较大的文件，不要直接调用read()
        # help(file_obj.read())
        # read()可以接受一个size作为参数，该参数用来指定要读取的字符的数量
        # 默认值是-1，它会读取文件中的所有字符
        # 可以为size指定一个值，这样read()会读取指定数量的字符
        #     每一次的读取都是从上一次读取到的位置开始读取的
        #     如果字符的数量小于size，则会读取剩余所有的
        # content = file_obj.read(-1)
        content = file_obj.read(6)
        content = file_obj.read(6)
        content = file_obj.read(6)
        content = file_obj.read(6)

        print(content)
        print(len(content))
except FileNotFoundError:
    print(f'{file_name} 文件不存在···')


