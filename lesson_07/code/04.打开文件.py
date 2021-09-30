# open(file, mode='r', buffering=-1, encoding_=None, errors=None, newline=None, closefd=True, opener=None)
# 使用open函数来打开一个文件
# 参数：
#   file 要打开的文件的名字(路径)
# 返回值
#   返回一个对象，这个对象就代表了当前打开的文件

# 创建一个变量，来保存文件的名字
# 如果目标文件和当前文件在同一级目录下，则直接使用文件名即可
file_name = 'demo.txt'
# 在Windows系统使用路径时，可以使用/来代替\
# file_name = 'hello/demo.txt'
# 或者使用\\来代替/
# file_name = 'hello\\demo.txt'
# 或者使用原始字符串
# file_name = r'hello\demo.txt'

# 表示路径，可以使用..来返回一级目录
# file_name = '../hello/demo.txt'

# 如果目标路径距离当前文件比较远，此时可以使用绝对路径
# 绝对路径应该从磁盘的根目录开始书写
file_name = 'C:/Users/Administrator/Desktop/test.txt'

file_obj = open(file_name)

print(file_obj)






