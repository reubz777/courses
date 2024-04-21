first_list = []
for i in range(100):
    my_str = input("Введите значение: ")
    if my_str == "stop":
        print("Вы ввели первый набор чисел")
        break
    else:
        first_list.append(my_str)

second_list = []
for i in range(100):
    my_str = input("Введите значение: ")
    if my_str == "stop":
        print("Вы ввели второй набор чисел")
        break
    else:
        second_list.append(my_str)

first_number = []
second_number = []

# Сравнение
for i in first_list:
    for j in second_list:
        if i == j:
            first_number.append(i)

# Числа которые присудствуют в обоих наборах
toghether_number = []
for i in first_number:
    if i not in toghether_number:
        toghether_number.append(i)
print(f"Числа которые присудствуют в обоих наборах: {toghether_number}")

different_number_1 = []
for i in first_list:
    if i not in second_list:
        different_number_1.append(i)

different_number_2 = []
for i in second_list:
    if i not in first_list:
        different_number_2.append(i)

print(f"Числа которых нету во втором наборе: {different_number_1}")
print(f"Числа которых нету в первом наборе: {different_number_2}")