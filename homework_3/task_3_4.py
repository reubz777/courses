N = 3
M = 3
mass = []
finally_mass = []
for i in range(N):
    mass.append([0]*M)
    finally_mass.append(0)
for i in range(N):
    for j in range(M):
        mass[i][j] = input("Введите значени: ")
print(mass)

for i in range(0 , N):
    for j in range(0 , M):
        finally_mass[i] += int(mass[j][i])

print(finally_mass)