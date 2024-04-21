new_str = input("Введите строку: ")
count = 1
result = ''
for ind, elem in enumerate(new_str):
    if new_str[ind:ind + 1] == new_str[ind + 1:ind + 2]:
        count += 1
    else:
        result += elem + str(count)
        count = 1
print(result)
