name_list = []
phone_list = []
email_list = []
print("Выберете 1 что бы добавить новый контакт")
print("Выберете 2 что бы удалить новый контакт")
print("Выберете 3 что бы просмотреть все контакты")
print("Выберете 4 что бы посмотреть информацию о конкретном контакте")
print("Выберете 5 что бы выйти из программы")

for i in range(1000):
    count = int(input("Введите номер операции: "))
    if count == 1:
        new_name = input("Введите имя нового контакта: ")
        new_phone = input("Введите номер телефона нового контакта в формате хх-хх-х: ")
        new_email = input("Введите почту нового контакт: ")
        name_list.append(new_name)
        phone_list.append(new_phone)
        email_list.append(new_email)
    if count == 2:
        name_dell = input("Введите имя контакта который хотите удалить: ")
        index_count = name_list.index(name_dell)
        name_list.remove(name_dell)
        phone_list.pop(index_count)
        email_list.pop(index_count)
    if count == 3:
        for i in range(len(name_list)):
            print(f"Имя: {name_list[i]} | Номер телефона: {phone_list[i]} | Почта: {email_list[i]}")
    if count == 4:
        name_chek = input("Введите имя контакта, для вывода информации о нём: ")
        name_index_to_chek = name_list.index(name_chek)
        print(f"Номер телефона: {phone_list[name_index_to_chek]} | Почта: {email_list[name_index_to_chek]} ")
    if count == 5:
        print("ВЫ ВЫШЛИ ИЗ ПРОГРАММЫ!")
        break
