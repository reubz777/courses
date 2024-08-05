import os.path
from os import path
import json
import random

class Bank():

    # Инициализация объекта
    def __init__(self, id, client_name, account_number):
        self.client_name = client_name
        self.account_number = account_number
        self.id = id

    # Резервная БД(открытие)
    def id_method(dict_test):
        with open("id.json", "w") as fh:
            json.dump(dict_test, fh)

    # Резервная БД(закрытие)
    def open_id():
        with open("id.json", "r") as fh:
            return json.load(fh)

    # открытие закрытие
    def id_serialize(dict):
        Bank.id_method(dict)
        Bank.open_id()

    # Рабочая БД(открытие)
    def json_method(dict_test):
        with open("data.json", "w") as fh:
            json.dump(dict_test, fh)

    # Рабочая БД(закрытие)
    def open_json():
        with open("data.json", "r") as fh:
            return json.load(fh)

    # открытие закрытие
    def json_serialize(dict):
        Bank.id_method(dict)
        Bank.open_id()

    # Проверка существует ли файл id.json, если нет - создаем файл, что бы не ловить ошибку в datafile
    def file_examination():
        if path.exists("id.json") == False:
            data = []
            Bank.id_method(data)

    # Проверяет есть ли в резервном datafile что-то, если он не пуст, то копирует данные в рабочий datafile
    def database_method():
        data = Bank.open_id()
        if len(data) == 0:
            data = []
            Bank.json_method(data)
        else:
            data = Bank.open_id()
            Bank.json_method(data)
            Bank.open_json()

    # Генратор номера счёта состоящий из 10 символов
    def gen_account_number():
        account_number = ""
        for i in range(10):
            account_number += str(random.randint(0, 9))
        return int(account_number)

    # Копирование при запуске программы.
    def json_copy():
        Bank.open_id()
        data = Bank.open_id()
        database = []
        for i in data:
            database.append(i)
        Bank.json_serialize(database)
        Bank.id_serialize(database)

    # Метод добавление листа
    def list_add(data: list, obj: object):
        return data.append(obj)

    # Удаляет элементы из дб если пользовательл ввел не корректные данные
    def examination_after_add():
        data = Bank.open_id()
        if Bank.name_processing(data[len(data) - 1]["Имя клиента"]).isdigit() == True:
            data.pop()
            print("Некорректный ввод данных")
            Bank.id_method(data)

    # функция для обработки имени
    def name_processing(name):
        count_str = ""
        for i in name:
            if 64 < ord(i) < 92 or 96 < ord(i) < 123 or ord(i) == " ":
                continue
            else:
                count_str += "1"
        return count_str

    # Валидация на ввод имя пользователя
    def error_handling(client_name):
        name = client_name
        count_str = Bank.name_processing(name)
        if count_str.isdigit() == False:
            return Menu_Bank.choose_value()
        else:
            return False

    # Добавление объекта в БД
    def object_add():
        obj = Bank(id=len(Bank.open_id()) + 1,
                   client_name=input("Введите имя клиента (имя должно содержать в себе только латинские буквы): "),
                   account_number=Bank.gen_account_number())
        dict_struct = {"id": obj.id, "Имя клиента": obj.client_name,
                       "Номер счёта": {obj.account_number: {Bank.error_handling(obj.client_name): 0}}}
        data = Bank.open_json()

        def add(data: list):
            return data.append(dict_struct)

        add(data)
        Bank.id_serialize(data)
        Bank.json_serialize(data)
        Bank.examination_after_add()


class Menu_Bank(Bank):

    # обработка ввода
    def correct_input(value: str, left_value, right_value):
        if value.isdigit() == True and int(value) >= left_value and int(value) <= right_value:
            return int(value)
        else:
            print("""
        Вы ввели некорректные данные.    
          """)
            return False

    # Валидация валюты
    def validation_value():
        pass

    def menu_output():
        print("""
        -----------------------------------------------------         
        | 1. Открыть счет для клиента.                       |
        | 2. Закрыть счет клиента.                           |
        | 3. Пополнить банковский счет.                      |
        | 4. Снять сумму со счета.                           |
        | 5. Перевести деньги между счетами.                 |
        | 6. Добавить валюту к клиенту.                      |
        | 7. Информация об клиентах.                         |
        | 8. Выход из программы.                             |
        -----------------------------------------------------                 
    """)

    # Поиск клиента
    def serch_client():
        data = Bank.open_id()
        serch_name = input("Введите имя: ")
        for i in data:
            if i["Имя клиента"] == serch_name:
                return data.index(i)

    # получаем номер аккаунта в виде строки {"9563322014": {"USD": 1000}}
    def output_key(str_number, value):
        for i in str_number:
            for j in str_number[i]:
                if j == value:
                    return i

    # декоратор для пополения/снятия денег со счёта
    def deco_add_take_money(fun):
        def wrapper(*args, **kwargs):
            result = fun(*args, *kwargs)
            if Menu_Bank.examination_INT(result) is True:
                data = Bank.open_id()
                index = Menu_Bank.serch_client()
                if type(index) == int:
                    str_number = data[index]["Номер счёта"]
                    value = Menu_Bank.choose_value()
                    number_bank_acc = Menu_Bank.output_key(str_number, value)
                    data[index]["Номер счёта"][number_bank_acc][value] += int(result)
                    Bank.id_method(data)
                else:
                    return print("Такого клиента не существует")

            else:
                return print("Сумма пополнения должна состоять из цифр")
            return result

        return wrapper

    # Выбор валюты
    def choose_value():
        print("""         
        1. russian_ruble
        2. american_dollar
        3. belarussian_ruble     
""")
        value = input("Выберите валюту: ")
        result_value = Menu_Bank.correct_input(value, 1, 3)
        if result_value == 1:
            return "RUS"

        if result_value == 2:
            return "USD"

        if result_value == 3:
            return "BYN"

    # Провверка добавление нового счёта
    def validation_value(data: list, value: str, index: int):
        for i in data[index]["Номер счёта"]:
            for j in data[index]["Номер счёта"][i]:
                if j == value:
                    return True
                else:
                    return False

    def examination_INT(number: str):
        if number[0] == "-" and number[1:].isdigit() or number.isdigit():
            return True

    # Меню вариации
    def menu_logic(res_menu):
        if res_menu == 1:
            Bank.object_add()
        if res_menu == 2:
            data = Bank.open_id()

            def del_client(data: list):
                index = Menu_Bank.serch_client()
                if type(index) == int:
                    print(f"Клиент {data[index]["Имя клиента"]} удалён")
                    return data.pop(index)
                else:
                    return print("Такого клиента не существует")

            del_client(data)
            Bank.id_method(data)
        if res_menu == 3:
            @Menu_Bank.deco_add_take_money
            def add_money(money_count=input("Введите сумму пополнения: ")):
                return money_count

            add_money()
        if res_menu == 4:
            @Menu_Bank.deco_add_take_money
            def take_off_money(money_count=input("Введите сумму которую желаете списать со счёта: ")):
                money_count = "-" + money_count
                return money_count

            take_off_money()
        if res_menu == 5:
            data = Bank.open_id()
            transaction_money = input("Введите сумму которую желаете перевести: ")

            def transaction_operation(str_number: dict, value: str):
                for i in str_number:
                    if value in str_number[i]:
                        return True
                        # Транзакция между аккаунтами

            def transaction(transaction_money):
                if Menu_Bank.examination_INT(transaction_money) is True:
                    first_index = Menu_Bank.serch_client()
                    seconde_index = Menu_Bank.serch_client()
                    if type(first_index) == int:
                        if type(seconde_index) == int:
                            value = Menu_Bank.choose_value()
                            first_str_number = data[first_index]["Номер счёта"]
                            seconde_str_number = data[seconde_index]["Номер счёта"]
                            if transaction_operation(first_str_number, value) and transaction_operation(
                                    seconde_str_number, value):
                                first_number_bank_acc = Menu_Bank.output_key(first_str_number, value)
                                seconde_number_bank_acc = Menu_Bank.output_key(seconde_str_number, value)
                                data[first_index]["Номер счёта"][first_number_bank_acc][value] -= int(transaction_money)
                                data[seconde_index]["Номер счёта"][seconde_number_bank_acc][value] += int(
                                    transaction_money)
                            else:
                                return print("ОШИБКА ПЕРЕВОДА: откройте счёт для того что бы переводить")
                        else:
                            return print("Такого клиента не существует")
                    else:
                        return print("Такого клиента не существует")

                else:
                    print("Вы ввели некорректные данные")

            transaction(transaction_money)
            Bank.id_method(data)
        if res_menu == 6:
            def add_account_num():
                data = Bank.open_id()
                index = Menu_Bank.serch_client()
                value = Menu_Bank.choose_value()
                if Menu_Bank.validation_value(data, value, index) == True:
                    print("Такой счёт уже существует")
                else:
                    data[index]["Номер счёта"][Bank.gen_account_number()] = {value: 0}
                Bank.id_method(data)

            add_account_num()
        if res_menu == 7:
            print("Выгружаем данные с БД...")
            data = Bank.open_id()
            for i in data:
                print(f"""
{i}""")
        if res_menu == 8:
            return False

    # input menu
    def menu():
        Menu_Bank.menu_output()
        menu_input = input("Выберите операцию: ")
        res_input = Menu_Bank.correct_input(menu_input, 1, 8)
        return res_input

    def start_program():
        Bank.file_examination()
        Bank.database_method()
        Bank.json_copy()

def start():
    print("""Добро пожаловать в admin панель. """)
    while True:
        Menu_Bank.start_program()
        variation = Menu_Bank.menu()
        if variation != 8:
            Menu_Bank.menu_logic(variation)
        else:
            break

start()