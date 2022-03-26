"""В матрице элементы второго столбца заменить элементами из одномерного динамического массива соответствующей
размерности."""
from random import randint


m = int(input("Введите число строк матрицы "))
n = int(input("Введите число столбцов матрицы "))


matrix = [[randint(0, 10) for j in range(n)] for i in range(m)]
list = [randint(-10, 0) for x in range(m)]
print(matrix)
print(list)
for i in range(m):
    print('Элемент матрицы', matrix[i][1])
    print(list[i])
    matrix[i][1] = list[i]

print(matrix)
