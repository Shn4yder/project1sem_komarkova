"""
Дано два целых числа А и В. Проверить истинность высказывания: " Хотя бы одно из чисел А и В нечетное "
"""

a = input('Введите число A: ')
b = input('Введите число B: ')


while type(a) != int:                                       # обработка исключений для числа А
    try:
         a = int(a)
    except ValueError:
        print('Вы ввели нецелое число А')
        a = input('Введите число A: ')


while type(b) != int:                                        # обработка исключений для числа В
    try:
         b = int(b)
    except ValueError:
        print('Вы ввели нецелое число В')
        a = input('Введите число B: ')


if (a % 2 == 1) or (b % 2 == 1):
    print('Данное высказывание истинно')
else:
    print('Данное высказывание неверно')