with open('demo.txt','rb') as file_obj:

# seek() 可以修改当前读取的位置
    file_obj.seek(55)
    file_obj.seek(80,0)
    file_obj.seek(70,1)
    file_obj.seek(-10,1)
# seek() 需要两个参数
#     第一个 是要切换到的位置
#     第二个 计算位置方式
#            可选值：
#                 0 从头计算，默认值
#                 1 从当前位置计算
#                 2 从最后位置开始计算

    print(file_obj.read())

# tell() 方法用来查看当前读取的位置
    print('当前读到了 -->',file_obj.tell())






