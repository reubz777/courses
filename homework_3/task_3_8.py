array = [5, 7, 4, 3, 8, 2]

for run in range(len(array)-1):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]

print(array)