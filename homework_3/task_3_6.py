new_list = []
N = int(input("Введите число: "))
for i in range(100):
    i = input("Введите значение элемента списка: ")
    if i == "stop":
        break
    else:
        new_list.append(int(i))

new_list.sort()
print(f"Список: {new_list}")
index_number = []
for i in range(len(new_list)):
    if new_list[i] == N:
        index_number.append(i)

if range(len(index_number)) != 0:
    print(f"Цифра {N} находится под индекс(ами): {index_number}")
else:
    print(f"Цифра {N} находится под индексом: -1")