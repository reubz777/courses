from datetime import datetime
import os

def log_calls(fun):
    def wrapper(name_file):
        time_now = str(datetime.now())
        with open(name_file, "a+") as file:
            file.write(f"Время вызова функции: {time_now} Имя вызванной функции: {fun.__name__} Аргумент вызванной функции {name_file} \n" )
        return fun(name_file)
    return wrapper

name_file = os.path.basename("text.txt")

@log_calls
def deco_func_task(res):
    """Для проверки"""
    with open(name_file, "r") as file:
        log_file = file.read()
        print(log_file)
    return res

deco_func_task(name_file)


