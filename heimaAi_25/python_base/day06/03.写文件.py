"""
    写文件
        write(data) 文件中写数据
        writelines() 一次写多行
    细节:
        write 覆盖写
        读的时候,如果文件不存在则报错
        写的时候,如果目的地文件不存在,会自动创建
"""

f = open("./files/c.txt","w",encoding="utf-8")
f.write("hello world")
f.write("傻逼python")
f.close()