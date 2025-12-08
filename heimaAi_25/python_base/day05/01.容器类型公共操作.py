"""
     容器类行的公共运算符解释：
        概述：
    公共运算符：
        +       表示：合并（拼接）可多用于： 字符串、列表、元组
        *       表示：复制 可作用于：字符串、列表、元组
        in      表示：是否在 可作用于：字符串、列表、元组、字典
        not in  表示：是否不在 可作用于：字符串、列表、元组、字典
    公共函数：
        len() 容器长度
        del 删除
        max() 返回最大值
        min() 返回最小值
        range(start.end,step) 生成从 start 到 end 的数字，步长为 step，供 for 循环使用
        enumerate() 将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同事列出的数据和数据下标
"""

str2 = "123"
list1 = [1,2,3]
# tem1 = (1,2,3)
# str2 = str+"111"
# print((1,2,3)+(4,))

print(enumerate(list1))
for index,item in enumerate(list1):
    print(index,item)

# print(list(range(1,5,1)))
#