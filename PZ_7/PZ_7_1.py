"""
Дано четное число N (N>0) и символы С1 и С2. Вывести строку длины N, которая состоит из чередующихся символов С1 и С2,
начиная с С1
"""
c1 = input('Введите первый символ строки:  ')
c2 = input('Введите второй символ строки:  ')
n = int(input('Введите длину строки:  '))

if n % 2 == 0:
    print('Ваша строка: ',(c1 + c2) * int(n / 2))
else:
    print('Значение длины строки должно быть четным')
