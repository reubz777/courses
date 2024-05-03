import random

def generetoon_mass(size_N_mass, size_M_mass):
    lst = [[j for j in range(size_N_mass)] for i in range(size_M_mass)]
    return lst

size_N = int(input("Введите первую сторону матрицы: "))
size_M = int(input("Введите вторую сторону матрицы: "))
original_mass = generetoon_mass(size_N, size_M)
finally_transpose_mass = [[] for i in range(len(original_mass[0]))]

def outputt_original_mass(mass):
    print("Оригинальная матрицы: ")
    for i in mass:
        print(i)

def transpose_algoritm(first_mass,second_mass):
    for i in range(len(first_mass[0])):
        for j in range(size_M):
            second_mass[i].append(first_mass[j][i])


def outputt_transpose_mass(mass):
    print("Транспортированная матрица: ")
    for i in mass:
        print(i)

outputt_original_mass(original_mass)
transpose_algoritm(original_mass, finally_transpose_mass)
outputt_transpose_mass(finally_transpose_mass)