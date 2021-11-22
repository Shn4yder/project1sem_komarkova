"""
Даны целые положительные числа А и В (А>B).На отрезке длины А размещено максимально возможное количетсво отрезков
длины В (без наложений).Используя операцию деления нацело, найти количество отрезков В, размещенных на отрезке А
"""

a = input('Введите значение отрезка A: ')
b = input('Введите значение отрезка B: ')


while type(a) != int:                                       # обработка исключений для отрезка А
    try:
         a = int(a)
    except ValueError:
        print('Вы ввели нецелое значение отрезка А')
        a = input('Введите целое значение отрезка A: ')


while type(b) != int:                                        # обработка исключений для отрезка В
    try:
         b = int(b)
    except ValueError:
        print('Вы ввели нецелое значение отрезка В')
        a = input('Введите целое значение отрезка B: ')


if a <= 0 or b <= 0:
    print('Отрезки А и В должны быть ТОЛЬКО положительными')
elif a <= b:
    print('Отрезок А должен быть больше отрезка В')
else:
    print('Количество отрезков В, размещенных на отрезке А: ', a//b)
