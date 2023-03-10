# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста 
# есть ровно два соседних. Всего на грядке растет N кустов. 
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
# различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1 )

# Output: 9

import random
N = int(input('Введите количество кустов на грядке: '))
m = []
for num in range(N):
    random_number = random.randint(0, 20)
    m.append(random_number)
print('Количество ягод на кустах: ', m)

max_count = 0
for i in range(len(m) - 1):
    max_count = max(max_count, m[i - 1] + m[i] + m[i + 1])

print(f'Максимальное число ягод, которое можно собрать за один заход с трех соседних кустов: ', {max_count})