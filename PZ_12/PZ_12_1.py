from tkinter import *
from tkinter.font import BOLD

# общее окно
root = Tk()
root.geometry('570x580')
root['bg'] = '#ed401e'

# плашка для формы
Canvas(root, bg="#660e00", height=470, width=320, highlightbackground="#660e00").place(x=130, y=100)

Label(
      text='html5 forms demo', width=25, height=1, bg='#ed401e', fg='white', font=('helvetica', "36", BOLD)
).place(x=-81, y=3)

Label(text='First Name', width=7, height=1, bg="#660e00", fg='white', font='Arial 10').place(x=145, y=105)
Entry(textvariable=StringVar(value='First Name'), fg='gray', width=32, font='arial 13').place(x=142, y=127)

Label(text='Last Name', width=7, height=1, bg="#660e00", fg='white', font='Arial 10').place(x=145, y=165)
Entry(textvariable=StringVar(value='Last Name'), fg='gray', width=32, font='arial 13').place(x=142, y=187)

Label(text='Email address', width=10, height=1, bg="#660e00", fg='white', font='Arial 10').place(x=143, y=225)
Entry(textvariable=StringVar(value='anything@example.com'), fg='gray', width=32, font='arial 13').place(x=142, y=247)

Label(text='Date of birthday (we like to send presents!)', width=33, height=1, bg="#660e00"
      , fg='white', font='Arial 10').place(x=134, y=280)
Spinbox(root, to=31, width=25).place(x=144, y=300)

Label(text='Country', width=5, height=1, bg="#660e00", fg='white', font='Arial 10').place(x=145, y=330)
Entry(width=26, font='arial 15').place(x=143, y=350)

Label(text='How many computers do you have at home?', width=32, height=1, bg="#660e00", fg='white',
font='Arial 10').place(x=145, y=390)
Spinbox(root, from_=1, to=10, width=25).place(x=144, y=410)

Label(text='We lowe spam, and well share you email address witch all ou: third-party friends.', width=64, height=1,
      bg="#660e00", fg='white', font='Arial 5').place(x=145, y=450)
Label(text='Heck, well even it! If yuore happy to receive annoying email on a regular basis', width=62, height=1,
      bg="#660e00", fg='white', font='Arial 5').place(x=145, y=460)
Label(text='please click submit..', width=16, height=1,
      bg="#660e00", fg='white', font='Arial 5').place(x=145, y=470)
Label(text='denotes a required field.', width=18, height=1,
      bg="#660e00", fg='white', font='Arial 5').place(x=150, y=490)

Button(text="Sign me up!", bg='#ff8f00', fg='white', width=10, font='Arial 13').place(x=335, y=520)
root.mainloop()
