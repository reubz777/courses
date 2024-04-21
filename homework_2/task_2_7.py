new_str = input("Введите значение: ")
N = int(input("Введите количество символов для шифра: "))
if N > 25:
    N = N % 25
new_mass = []
for i in new_str:
    new_mass.append(ord(i))

second_mass = []
for i in range(len(new_mass)):
    if int(new_mass[i])+N > 122:
        Z = (int(new_mass[i])+N) - 122
        second_mass.append(96 + Z)
    else:
        second_mass.append(new_mass[i]+N)

finally_mass = []
for i in second_mass:
    finally_mass.append(chr(i))
print(f"Зашифрованный текст: {finally_mass}")
