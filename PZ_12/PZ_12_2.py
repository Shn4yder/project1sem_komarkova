"""
Дан целочисленный список размера 10. Вывести вначале все содержащиеся в данном списке четные числа в порядке возрастания
их индексов, а затем — все нечетные числа в порядке убывания их индексов.
"""
from tkinter import *

root = Tk()
root.title('Четные/ нечетные элементы списка')
root.geometry('600x200+400+200')

def obrabotchik(event):
    list = [int(i) for i in l.get().split(',')]

    list_chet = []
    list_nechet = []

    for element in list:  # перебор элементов
        if element % 2 == 0:
            list_chet.append(element)
        else:
            list_nechet.append(element)

    chet['text'] = f"Четные элементы списка: {str(list_chet).replace('[', '').replace(']', '')}"
    nechet['text'] = f"Нечетные элементы списка с конца: {str(list_nechet[::-1]).replace('[', '').replace(']', '')}"

Label(text="Введите список через запятую без пробелов").grid(row=0, column=0)
l = Entry()
l.grid(row=0, column=1)


button1 = Button(text="Сгенерировать!")
button1.grid(row=1, column=1)

button1.bind('<Button-1>', obrabotchik)

chet = Label()
chet.grid(row=2, column=1)

nechet = Label()
nechet.grid(row=3, column=1)

root.mainloop()


