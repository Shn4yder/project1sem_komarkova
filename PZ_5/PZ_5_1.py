"""
Составить функцию, генеирующую четырехзначное число и определяющую, есть ли в числе одинаковые числа.
"""


def generator(a, b, c, d):
    number = str(a) + str(b) + str(c) + str(d)
    if (a == b) or (a == c) or (a == d ) or (b == c) or (b == d) or (c == d):
        ravenstvo = 'В Вашем числе есть одинаковые цифры'
    else:
        ravenstvo = 'В Вашем числе нет одинаковых цифр'
    print('Ваше число:  ', number)
    print(ravenstvo)


num1 = int(input('Введите первую цифру  '))
num2 = int(input('Введите вторую цифру  '))
num3 = int(input('Введите третью цифру  '))
num4 = int(input('Введите четвертую цифру  '))


generator(num1, num2, num3, num4)


























