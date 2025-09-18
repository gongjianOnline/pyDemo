"""
os 模块介绍:
    概述:
        全称: Opearting System 系统模块,主要是操作 文件夹\文件\路径等
    常用函数:
        getcwd() 获取当前的工作空间目录
        chdir() 改变工作空间路径
        rmdir() 删除文件夹,必须是空文件
        rename() 改名,文件/目录都可以
        listdir() 获取指定目录下 所有的子集文件或者文件夹(不包括子集的子集)
"""

import os

print(os.getcwd())
# os.chdir('C:/my/files/code')
# f = open('1.txt', 'r', encoding='utf-8')
# print(f.read())
# f.close()
# os.mkdir("file")
# os.rmdir("file")
# os.rename("file","newfile")
print(os.listdir())