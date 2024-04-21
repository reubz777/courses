import random

random_int = random.randint(0, 100)
print(f"Сгенерированое число (Для преподавателя) : {random_int}")

examination_count = "0543210"
for i in range(1, 7):
    examination = int(input("Попробуйте угадать число: "))
    if random_int == examination:
        print("Вы угадали число")
        break
    else:
        print(f"У вас осталось {examination_count[i]} попыток")
        if examination_count[i] == "0":
            print(" У вас не удалось отгадать. Попробуйте снова")
            break
        if examination > random_int:
            print(f"Число меньше, чем {examination}")
        else:
            print(f"Число больше, чем {examination} ")