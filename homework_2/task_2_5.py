first_str = input("Введите первое слово:")
second_str = input("Введите второе слово: ")
first_list = list(first_str)
second_list = list(second_str)
first_list.sort()
second_list.sort()
if first_list == second_list:
    print("Слова являются анаграммами")
else:
    print("Слова не являются анаграммами")
