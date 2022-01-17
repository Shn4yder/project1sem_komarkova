"""
Из предложенного текстового файла (text18-9.txt) вывести на экран его содержимое, количество букв в нижнем регистре.
Сформировать новый файл, в который поместить текст в стихотворной форме предварительно поставив последнюю строку фразой
введенной пользователем
"""
import string


text = open('text18-9.txt', encoding="utf8").read()   # чтение текста из файла и трансляция его в консоль
print(text)

for p in string.punctuation + '\n':    # удаление пунктуации для последующего подсчета букв
    if p in text:
        text = text.replace(p, '')
count = 0
for letter in text.replace(" ", ""):   # подсчет строчных букв
    if letter.islower():
        count += 1
print('Строчных букв в исходном файле', count)

print(open('text18-9.txt', encoding="utf8").read(158), file=open('new_file.txt', 'w'))

with open('new_file.txt', 'a') as f_in:
    f_in.write(input('Введите строку для записи последней строкой: '))




