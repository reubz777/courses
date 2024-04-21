my_str = input("Введите предлоежение ")
my_str = my_str.replace(" ", "")
new_word = ""
for x in my_str:
   if x not in new_word:
      new_word += x

print(new_word)