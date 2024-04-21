import random

new_pass = []
examination_count = []
N = int(input("Введите размер генерируемого пароля: "))
new_str = ".*^_()[]{,}?!@"
if N < 4:
    print("Пароль не может содержать менее 4-х символов")
else:
    for i in range(int(N)):
        primary_random = random.randint(1,4)
        if primary_random == 1:
            examination_count.append(1)
            new_str_metod = random.randint(0, len(new_str)-1)
            new_pass.append(new_str[new_str_metod])
        if primary_random == 2:
            examination_count.append(2)
            small_alphabet = random.randint(97, 122)
            new_pass.append(chr(small_alphabet))
        if primary_random == 3:
            examination_count.append(3)
            big_alphabet = random.randint(65, 90)
            new_pass.append(chr(big_alphabet))
        if primary_random == 4:
            examination_count.append(4)
            new_pass.append(random.randint(0, 9))

    # проверка соблюдаются ли условия

    if 1 not in examination_count or 2 not in examination_count or 3 not in examination_count or 4 not in examination_count:
            count_1 = random.randint(0, N-4)
            count_2 = random.randint(count_1+1, N-3)
            count_3 = random.randint(count_2+1, N-2)
            count_4 = random.randint(count_3+1, N-1)
            new_str_metod = random.randint(0, len(new_str)-1)
            new_pass[count_1] = new_str[new_str_metod]
            small_alphabet = random.randint(97, 122)
            new_pass[count_2] = chr(small_alphabet)
            big_alphabet = random.randint(65, 90)
            new_pass[count_3] = chr(big_alphabet)
            new_pass[count_4] = random.randint(0, 9)
    finally_pass = ""
    for i in new_pass:
         finally_pass += str(i)
    print(f"Сгенерированный пароль: {finally_pass}")
