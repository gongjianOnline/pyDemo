"""
    with-open语句
        主要用于对文件的操作,即 不需要手动 close() 释放资源,该语句执行完成后,自动释放
    格式:
        with open("路径","模式","码表") as 别名 :
            语句体
"""

with  open("./files/b.txt","rb") as  read_f , open("./files/E.txt","wb") as write_f:
    write_f.write(read_f.read())