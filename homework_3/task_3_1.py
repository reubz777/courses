number = int(input("ВВедите число: "))
faktor = 1
for i in range(number):
    faktor *= (i+1)

print(f"Факториал числа {number} равняется: {faktor}")