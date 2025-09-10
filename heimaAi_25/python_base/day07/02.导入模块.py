"""
    导入方式
        import 模块名                          后续通过 模块名.函数名() 调用
        import 模块名 as 别名                   后续通过 别名.函数名() 调用
        from 模块名 import 函数名               后续通过 函数名() 调用
        from 模块名 import 函数名 as 别名        后续通过 别名() 调用
        from 模块名 import *                   后续通过 函数名() 调用
"""

import random
from time import sleep
from my_module import myAdd

print("2222")
sleep(10)
print("11111")
myAdd(1,2)