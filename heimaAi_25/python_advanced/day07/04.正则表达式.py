"""
正则表达式：
    使用步骤：
        1. 导包
        import re
        2. 正则校验
        result = re.match(pattern=正则规则，str=要校验的字符串，flag=0)
        3. 获取匹配的数据
        result.group()
    正则表达式 涉及到的函数:
        1. 用于做校验的.替换的
            match() 全词匹配
            search() 部分满足
            compile().sub() 替换
        2. 用于 获取值的 .
            group()
"""


