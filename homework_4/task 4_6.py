original_list = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]

def deco_unique_element(fun):
    def wrapper(lst):
        finally_original_element_lst = []
        for i in fun(lst):
            if i in finally_original_element_lst:
                continue
            else:
                finally_original_element_lst.append(i)
        return finally_original_element_lst
    return wrapper

@deco_unique_element
def unique_elemets(lst):
    if not lst:
        return lst
    if isinstance(lst[0], list):
        return unique_elemets(lst[0]) + unique_elemets(lst[1:])
    return lst[:1] + unique_elemets(lst[1:])

print(unique_elemets(original_list))



