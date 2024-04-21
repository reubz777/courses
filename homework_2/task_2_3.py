word_list = []
for i in range(100):
    my_str = input("Введите слово: ")
    if my_str == "stop":
        print(f"Вы ввели {len(word_list)} слов(а)")
        break
    else:
        my_str = my_str.capitalize()
        word_list.append(my_str)


dict_word = dict()
for i in word_list:
    dict_word[i] = word_list.count(i)

print(dict_word)