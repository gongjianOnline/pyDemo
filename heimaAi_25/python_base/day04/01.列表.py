"""
CURD
增
    append(单个值 / 列表) 在末尾添加 ,如果添加 列表 整个添加
    extend(单个值 / 列表) 在末尾添加, 如果添加 列表 拍平后添加
    insert(索引值 ,要插入的元素) 在指定位置插入元素,如果索引不存在,默认在最后添加

查
    index(数据,[开始下标],[结束下标]) 返回下标,没有返回异常
    count() 出现的顺序
    in 判断指定数据是否在列表中，返回 booler
    not in 判断指定数据是否在列表中，返回 booler

删
    del 列表名     删除列表
    del 列表名[index] 根据索引删除元素
    列表名.clear[] 返回一个空列表
    列表名.pop(index) 根据下表删除
    列表名.remove(元素值) 根据元素删除

改
    list.reverse() 反转列表元素
    list.sort() 升序
    list.sort(reverse=True) 降序


"""
arr = ["aaa","bbb","ccc","ddd"]
#
# for item in arr:
#     print(item)

# arr.append(["222"])
# arr.extend(["222","333"])
# arr.insert(len(arr),100)
# print(arr)
# # print(arr.index("2222"))
# print("222" in arr)
# print("2222" not in arr)
# del arr[0]
arr.remove("aaa")
arr.pop(1)
print(arr)