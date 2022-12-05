# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
N = int(input())

a = []
for i in range(-N, N + 1):
    a.append(i)
print(a)

res = 1
with open('file.txt') as f:
    for i in f.readlines():
        res *= a[int(i)]

print(res)