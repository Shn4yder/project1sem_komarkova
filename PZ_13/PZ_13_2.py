"""
Из заданной строки отобразить только символы нижнего регистра. Использовать библиотеку string. Строка 'In PyCharm, you
can specify third-party standalone applications and run them as External Tools'
"""
from string import ascii_lowercase


string = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
print('Строчные буквы в строке без повторов', *set(letter for letter in string if letter in ascii_lowercase))
