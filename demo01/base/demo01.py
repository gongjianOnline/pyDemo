# for index in range(10):
#     print(index)

arr =  ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
if "Python" in arr:
    arr.remove("Python")

# print(arr.pop(1))
# print(arr.clear())
# print(arr.index("Java"))
print(arr.count('SQL'))

tupleInfo = tuple(arr)
print(tupleInfo)
print(list(tupleInfo))