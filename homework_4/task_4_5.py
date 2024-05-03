number = input("Введите какое-то число:")

dct = {str(element): element + 1 for element in range(3)}
print(f"Исходный список: {dct}")

def cash(func):
    def wrapper(num):
        result = func(num) 
        if num in dct:
            print(f"В списке {dct} присудствует ключ {num}")
        else:
            dct[num] = int(num)
            print(f"Так как ключа {num} не было в списке, добавим его. Результат добавление: {dct}")
        return result
    return wrapper

@cash
def functional_function(number):
    return number

functional_function(number)