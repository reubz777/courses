my_str = input("Введите слово: ")
new_str = ""
for i in range(len(my_str)):
    new_str += my_str[-(i+1)]
if my_str == new_str:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")


