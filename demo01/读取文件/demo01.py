# file = open('致橡树.txt','a+',encoding="utf-8");
# file.write('\n标题：《致橡树》')
# file.write('\n作者：舒婷')
# file.write('\n时间：1977年3月')
#
# print(file.read())
# file.close();

try:
    with open("致橡树.txt","rb") as file1:
        data = file1.read()
        print(data)
    with open("致橡树2.txt","wb") as file2:
        file2.write(data)
except FileNotFoundError:
    print("指定文件无法打开")
except IOError:
    print("读写文件时出错")