"""
Дана строка, содержащая полное имя файла, то есть имя диска,список каталогов (путь), собственно имя файла и расширение.
Выделить в этой строке имя файла без расширения.
"""
string = input('Введите полное имя файла:  ')
print(string)


if '.' in string:
    directories_list = string.split('\\')
    file = directories_list[-1]
    file_1 = file.split('.')
    print(file_1[0])
else:
    print('В Вашем пути нет имени файла')
