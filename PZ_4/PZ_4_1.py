"""
Дано целое число  N (>0). Найти сумму 1 + 1/2 + 1/2 + ... + 1/N.
"""

n = input('Введите число N:  ')


while type(n) != int:
    try:
         n = int(n)
    except ValueError:
        print('Вы ввели нецелое число N')
        n = input('Введите число N: ')
    if n == 0:
        print('Число N не должно равняться нулю')
        n = input('Введите ненулевое значение N: ')
        continue


summa = 0


while n > 0:
    summa = summa + 1/n
    n = n - 1
print('Сумма равна:', summa)
