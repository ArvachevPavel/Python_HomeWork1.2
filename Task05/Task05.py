# Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя, другие методы из библиотеки random - можно)
import random


N = int(input('Введите число: '))

a = []
for i in range(N + 1):
    a.append(i)

print('было:', a)

for i in range(random.randint(3, 7)):
    t1, t2 = random.randint(1, N), random.randint(1, N)
    a[t1], a[t2] = a[t2], a[t1]
    

print('cтало:', a)