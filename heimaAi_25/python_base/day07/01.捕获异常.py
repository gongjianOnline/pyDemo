"""
    基本句法
        try:
            可能出问题的语法
        except Exception as err:
            出问题后的解决方案
        else:
            如果没出问题执行的语法
        finally:
            怎么都会执行的语法

"""

try:
    xxx
except Exception as err:
    print("傻了吧",err)