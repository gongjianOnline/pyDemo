"""
    导入方式
        import 模块名                          后续通过 模块名.函数名() 调用
        import 模块名 as 别名                   后续通过 别名.函数名() 调用
        from 模块名 import 函数名               后续通过 函数名() 调用
        from 模块名 import 函数名 as 别名        后续通过 别名() 调用
        from 模块名 import *                   后续通过 函数名() 调用

    细节:
        1. 1个 .py 文件可以看做一个模块，文件名 = 模块名。所以：文件名也要符合的命名规范
        2. __name__属性，当前模块打印的结果是 __main__，在调用这中打印的结果是：调用的模块名
        3. 如果导入的多个模块中，有同名函数，默认会使用 最后导入的 模块的函数
        4. __all__ 属性只是针对 from 模块 import* 这种写法有效，他只会导入 __all__ 记录的内容

"""

import random
from time import sleep
from my_module import myAdd

print("2222")
sleep(10)
print("11111")
myAdd(1,2)