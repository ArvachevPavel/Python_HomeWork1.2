# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
a = int(input('Введите число: '))
composition = 1
for i in range(1, a+1):
    composition = composition * i
    print(composition, end=" ")


