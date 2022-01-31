"""
Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и
отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
1.Исходные данные:
2.Количество элементов:
3.Индекс последнего максимального элемента:
4.Меняем местами первую и последнюю трети:
"""
from random import randint

file_data = []     # генерация содрежимого исходного файла
count = 0
while count < 10:
    file_data.append(str(randint(-10, 10)))
    count += 1


print(",".join(file_data), file=open('file_10_1.txt', 'w'))     # запись содержимого в исходный файл

new_file = open('file_new10_1.txt', 'w')     # новый .txt файл
print('Исходные данные:', open('file_10_1.txt').read(), file=new_file)    # 1
print('Количество элементов:', len(open('file_10_1.txt').read().split(',')), file=new_file)    # 2


new_file_data = list(map(int, open('file_10_1.txt').read().split(',')))  # получение списка из файла с исходными данными
reverse = new_file_data[::-1]
print('Индекс последнего максимального элемента:', 9 - reverse.index(max(reverse)), file=new_file) #3

# меняем местами первую и последнюю трети
new_file_data[0], new_file_data[-3] = new_file_data[-3], new_file_data[0]
new_file_data[1], new_file_data[-2] = new_file_data[-2], new_file_data[1]
new_file_data[2], new_file_data[-1] = new_file_data[-1], new_file_data[2]


for n in range(0, len(new_file_data)):           # конвертация каждого элемента в строковый тип
    new_file_data[n] = str(new_file_data[n])

print('Измененные позиции первой и последней трети:', ",".join(new_file_data), file=new_file)    # 4

new_file.close()