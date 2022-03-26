"""В матрице найти среднее арифметичское положительных элементов, кратных трем"""
from random import randint


n = int(input("Введите число строк матрицы "))
m = int(input("Введите число столбцов матрицы "))

matrix = [[randint(-10, 10) for j in range(n)] for i in range(m)]
print('Исходная матрица')
for i in matrix:
    print(*i)

three = []
for i in matrix:
    for element in i:
        if element > 0 and element % 3 == 0:
            three.append(element)

if len(three) == 0:
    print('Элементов кратных трем не встретилось')
else:
    print('Среднее арифметическое положительных элементов:', sum(three) / len(three))

