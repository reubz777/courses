number_list = [0, 1]
finally_list = []
number = int(input("Введите число: "))

for i in range(2 , number):
    number_list.append(number_list[i-2]+number_list[i-1])

for i in number_list:
    if number > i:
        finally_list.append(i)
print(finally_list)
