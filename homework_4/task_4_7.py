import random

def sort_list_fun(lst):
    for j in range(len(lst)-1):
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1], lst[i]

def deco_sort(fun):
    def wrapper(*args):
        result = fun(*args)
        sort_list_fun(result)
        return result
    return wrapper

@deco_sort
def generate_lst(j):
    name = [random.randint(0,j) for i in range(j)]
    return name

@deco_sort
def merge_sort_list(fun1,fun2):
    return fun1+fun2

print(f"Отсортированный список после слияния: {merge_sort_list(generate_lst(10),generate_lst(5))}")


    
        