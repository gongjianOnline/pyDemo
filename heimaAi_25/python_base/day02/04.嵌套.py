balance = int(input("余额"))


if balance > 2:
    print("上公交")
    nullValue = input("是否有空座")
    if nullValue == '是':
        print("坐")
    else:
        print("站")
else:
    print("买票")