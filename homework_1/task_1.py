m = int(input("Введите количетсво рублей "))
n = int(input("Введите количество копеек "))
s = int(input("Введите общее количество товара "))
l = int(input("Сколько товаров заказал клиент? "))
n_rub = n//100
n_kop = (n % 100)/100
m = n_rub+m

print(n_kop)