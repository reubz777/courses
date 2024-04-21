
my_str = input("Введите предложение ")
my_str = my_str.strip('.')
my_str = my_str.replace(",", " ")
print(my_str)
my_str = my_str.split()
print(my_str)
max_word = ""
for x in my_str:
    if len(x) > len(max_word):
        max_word = x
print(max_word)
