"""
Дан целочисленный список размера 10. Вывести вначале все содержащиеся в данном списке четные числа в порядке возрастания
их индексов, а затем — все нечетные числа в порядке убывания их индексов. (для удобства проверки все списки выводятся на
экран)
"""

count = 0
list = []


while count < 10:                   # заполнение списка числами пользователя
    list.append(int(input('Введите число для заполнения списка: ')))
    count += 1

print('Ваш список:  ',list)


print('Четные элементы Вашего списка')
for element in list:                # перебор элементов. Вывод четных
    if element % 2 == 0:
        print(element)


print('Нечетные элементы Вашего списка')
for element in list[::-1]:           # перебор элементов. Вывод нечетных с конца
    if element % 2 == 1:
        print(element)
