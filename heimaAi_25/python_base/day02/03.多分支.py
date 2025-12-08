grades = int(input("成绩"))

if grades >= 90:
    print("游乐场")
elif 80 <= grades <= 89:
    print("游乐场半天")
elif 70 <= grades <= 79:
    print("博物馆")
elif 60 <= grades <= 69:
    print("练习题")
else:
    print("胖揍")