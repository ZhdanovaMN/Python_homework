# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

a = int(input("Введите первое целое неотрицательное число: "))
b = int(input("Введите второе целое неотрицательное число: "))

def sum(a, b):
    if (a == 0): return b
    return(sum(a-1, b+1))
print("Суммма a и b: ", sum(a, b))


