# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
a = int(input('Введите количество повторений: '))
n = int(input('Введите значение переменной: '))
sum = 0
for i in range(a):
    res = ((1 + 1 / n)**n)
    sum = sum + res
print('Сумма чисел равна: ',round(sum, 2))
