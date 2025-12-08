"""
    集合(set)
        集合里边的元素不可重复,等同于 JS 中的 Set,主要用于去重操作
    定义格式
        set1 = {1,2,3,"10"}
        set2 = set([1,2,3,"10"])
"""

# 列表去重
list1 = [1,2,3,1,1,1,1,1,1]
set_temp = set(list1)
print(list(set_temp))
