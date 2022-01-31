from tkinter import *

root = Tk()
root.title('Генератор чисел')
root.geometry('600x200+400+200')

def generator(event):
    a = num_1.get()
    b = num_2.get()
    c = num_3.get()
    d = num_4.get()

    number = a + b + c + d
    if (a == b) or (a == c) or (a == d) or (b == c) or (b == d) or (c == d):
        ravenstvo = 'есть одинаковые цифры'
    else:
        ravenstvo = 'нет одинаковых цифр'

    sravnenie['text'] = "В Вашем числе", ravenstvo
    num['text'] = "Ваше число", number



Label(text="Первое число").grid(row=0, column=0)
num_1 = Entry()
num_1.grid(row=0, column=1)
Label(text="Второе число").grid(row=1, column=0)
num_2 = Entry()
num_2.grid(row=1, column=1)
Label(text="Третье число").grid(row=2, column=0)
num_3 = Entry()
num_3.grid(row=2, column=1)
Label(text="Четвертое число").grid(row=3, column=0)
num_4 = Entry()
num_4.grid(row=3, column=1)

button1 = Button(text="Сгенерировать!")
button1.grid(row=4, column=1)

button1.bind('<Button-1>',generator)


sravnenie = Label()
sravnenie.grid(row=5, column=1)

num = Label()
num.grid(row=6, column=1)

root.mainloop()


root.mainloop()