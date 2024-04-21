N = int(input("Введите искаемое число: "))
array = [2, 3, 5, 5, 6, 12, 4, 1, 1, 15, 16, 16, 6]
array.sort()

print(f"Отсортированный список: {array}")

first_list = array[array.index(N):]
first_list.reverse()
second_list = first_list[first_list.index(N):]

count_N = len(second_list)

first_index = array.index(N)-1

for i in range(count_N):
    first_index += 1
    print(f" Число {N} находится под индекс(ами): {first_index}")