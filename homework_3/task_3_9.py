height = int(input("Введите высоту пиромиды: "))+2
symbol = input("Введите заполняемый символ: ")
symbol_tree = [[f"{symbol} "]]
tree = []

for i in range(1,height-1):
    tree.append(symbol_tree[0][0]*i)

space = " "
for i in tree:
    lengh_symbol = len(i)
    height_last_symbol = height*2
    space_count = int(((height_last_symbol-lengh_symbol)/2))
    space_count_finall = space_count*space
    print(f"{space_count_finall}{i}")
