"""
    字符串切片 [起始索引:结束索引:步长] (左开右闭)
    细节
    正向索引从前往后,从 0 开始
    如果不写起始索引,从 -1 开始
    如果 索引 和 步长的方向相反,获取不到数据
    不写结束索引,默认到最后
    [::-1] 表示反转字符串
    h e i m a I T
    0 1 2 3 4 5 6
"""

str = "heimaIT heimaIT"
print(str[0:5:2])

"""
常用API
find(子串,[开始位置下标],[结束位置下标]) 监测字符串是否包含,返回下标,否则返回-1 (同js indexOf)
index(子串,[开始位置下标],[结束位置下标]) 监测字符串是否包含,返回下标,否则返回异常
replace(旧串,新串,替换次数) 返回替换后的字符串
split() 字符串分割(同js)
len(str) 返回字符串长度
分隔符.join(str) 返回隔开字符串

"""

# print(str.find("i",3,6))
#
# print(str.replace("i","xxx",1))
#
# print(str.split(" "))
#
# print(",".join(str))
