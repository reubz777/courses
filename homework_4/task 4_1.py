list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]


def flatten_list(lst):
    if not lst:
        return lst
    if isinstance(lst[0], list):
        return flatten_list(lst[0]) + flatten_list(lst[1:])
    return lst[:1] + flatten_list(lst[1:])


print(flatten_list(list_a))