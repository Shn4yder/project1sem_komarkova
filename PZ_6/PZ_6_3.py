"""
Дано множество A из N точек на плоскости и точка B (точки заданы своими координатами х, у). Найти точку из множества A,
наиболее близкую к точке B. Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
R = √(x2 – x1)2+ (у2 – y1)2. Для хранения данных о каждом наборе точек следует использовать по два список: первый
список для хранения абсцисс, второй — для хранения ординат.(для удобства проверки все списки выводятся на экран)
"""
from math import sqrt
from random import randint

x = int(input('Введите значение абсциссы точки В '))
y = int(input('Введите значение ординаты точки В '))
n = int(input('Введите  количество точек  x и y:  '))


max_num = int(input('Введите максимальное значение для точек:  ')) + 1
abs_x = []       # список для абсцисс
ord_y = []       # список для ординат

count = 0

while count < n:            # заполнение списков
    abs_x.append(randint(0, max_num))
    ord_y.append(randint(0, max_num))
    count += 1

print('Список абсцисс:  ', abs_x)
print('Список ординат:  ', ord_y)

min_x = 0
min_y = 0

for i in range(0, len(abs_x) - 1):
    r = sqrt(((x - abs_x[i]) ** 2) + ((y - ord_y[i]) ** 2))  # рассчет расстояния между точками по формуле
    if r < max_num:
        max_num = r
        min_x = abs_x[i]
        min_y = ord_y[i]


print('Минимальное расстояние:  ', max_num)
print('Абсцисса самой близкой точки:  ',  min_x)
print('Ордината самой близкой точки:  ', min_y)
