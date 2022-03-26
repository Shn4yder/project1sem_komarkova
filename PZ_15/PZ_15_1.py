"""В матрице элементы второго столбца заменить элементами из одномерного динамического массива соответствующей
размерности."""
from random import randint


m = int(input("Введите число строк матрицы "))
n = int(input("Введите число столбцов матрицы "))


matrix = [[randint(0, 10) for j in range(n)] for i in range(m)]
list = [randint(-10, 0) for x in range(m)]
print('Список для обновления матрицы', list)
print('Исходная матрица')
for i in matrix:
    print(*i)

for i in range(m):
    matrix[i][1] = list[i]

print('Обновленная матрица')
for i in matrix:
    print(*i)
