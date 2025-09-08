"""
    文件打开
        open("url","打开模式",码表)
    文件读取
        read(num) 一次读取 num 字节,不写读全部
        readline() 一次读一行
        readlines() 读全部,且会把每行数据封装的列表中
    关闭文件
        文件对象名.close()
"""

f = open("./files/b.txt","r",encoding="utf-8")
print(f'文件对象{f}')
print(f.read())
f.close()