# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Введите число: '))
power = 1
while power <= N:
    print(power, end =' ')
    power = power * 2