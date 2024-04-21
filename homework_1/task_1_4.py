import math
side_1 = int(input("Введите первую сторону: "))
side_2 = int(input("Введите первую сторону: "))
side_3 = int(input("Введите первую сторону: "))
if side_1+side_2 <= side_3 or side_1+side_3 <= side_2 or side_2+side_3 <= side_1:
    print("Такого треугольника не существует")
else:
    s = 0
    p = (side_1+side_2+side_3)/2
    s = math.sqrt(p*(p-side_1)*(p-side_2)*(p-side_3))

    print(s)
