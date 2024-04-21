
new_list = []
for i in range(100):
    my_str = input("Введите значение: ")
    if my_str == "stop":
        break
    else:
        new_list.append(my_str)
print(new_list)

unique_list = []
repetitive_list = []
even_number = []
odd_numbers = []
negative_numbers = []
float_numbers = []
drop_nubmers = []
max_number = 0
min_number = 0
for i in new_list:
    if new_list.count(i) > 1:
        repetitive_list.append(i)
    else:
        unique_list.append(i)
    i = float(i)
    if i % 1 != 0:
        drop_nubmers.append(i)
    if i % 2 == 0:
        even_number.append(i)
    if i % 2 != 0:
        odd_numbers.append(i)
    if i < 0:
        negative_numbers.append(i)
    if i > max_number:
        max_number = i
    if i < min_number:
        min_number = i
print((f"Уникальные числа : {unique_list}"))
print((f"Повторяющиеся числа: {repetitive_list}"))
print((f"Четные числа: {even_number}"))
print((f"Нечетные числа: {odd_numbers}"))
print((f"Отрицательные числа: {negative_numbers}"))
print((f"Дробные числа: {drop_nubmers}"))
print((f"Максимальное число: {max_number}"))
print((f"Минимальное число: {min_number}"))

