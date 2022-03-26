"""В исходном текстовом файле (Dostoevsky.txt) найти все варианты фамилии Достоевского (т.е. с различными окончаниями,
например, Достоевский, Достоевского) в единственном экземпляре."""

import re


with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    Dostoevsky = file.read()
    print("Все вариации фамилии 'Достоевский' без повторов:", *set(re.findall(r"Достоевск[а-я]+", Dostoevsky)))
