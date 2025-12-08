"""
    推导式：
        python 特有写法
    分类：
        列表推导式
        集合推导式
        字典推导式
    格式
        变量名 = [变量名 for ... in ... if 判断条件]
        变量名 = {变量名 for ... in ... if 判断条件}
        变量名 = {变量名1:变量名2 for ... in ... if 判断条件}
"""

list1 = [index for index in range(10) if index%2]
print(list1)
set1 = {index*index for index in list1 }
print(set1)

list2 = ["name","age","gander"]
list3 = ["tom",20,"man"]
obj = {key:value for key,value in zip(list2,list3)}
print(obj)