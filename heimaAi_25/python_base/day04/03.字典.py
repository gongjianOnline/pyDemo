"""
    字典：
        存储键值对数据，数据可变类型
    定义格式：
        {key:value}

    查
        obj.get(key,[默认值])
        obj.keys() 获取所有key
        obj.values() 获取所有values
        obj.items() 把键值对变成元组,返回列表
"""

obj = {"name":"张三","age":"10"}
print(obj.items())

# for item in obj:
#     print(item,obj[item])