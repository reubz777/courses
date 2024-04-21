new_str = input('Введите предложение: ')
new_str = new_str.split()
print(new_str)
len_mysrt = len(new_str)
unique_mysrt = 0
for x in new_str:
    if new_str.count(x) == 1:
        unique_mysrt += 1

print(unique_mysrt)