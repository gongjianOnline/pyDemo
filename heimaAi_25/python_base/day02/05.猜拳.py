import  random
number = int(input("出拳"))
value =  random.randint(1, 3)

if number <= 3:
    if (number == 1 and value == 2) or (number == 2 and value == 3) or (number == 3 and value == 1):
        print("玩家赢")
    elif number == value:
        print("平局")
    else:
        print("电脑赢")
else:
    print("出老千")

