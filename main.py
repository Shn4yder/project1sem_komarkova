import tkinter as tk
import tkinter.ttk as ttk
import sqlite3 as sq
from BD.Child import Child


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="BD/11.gif")
        btn_open_dialog = tk.Button(toolbar, text='Добавить игрока', command=self.open_dialog, bg='#5da130', bd=0,
                                    compound=tk.TOP, image=self.add_img )
        btn_open_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('user_id', 'name', 'sex', 'old', 'score'), height=15, show='headings')

        self.tree.column('user_id', width=50, anchor=tk.CENTER)
        self.tree.column('name', width=180, anchor=tk.CENTER)
        self.tree.column('sex', width=140, anchor=tk.CENTER)
        self.tree.column('old', width=140, anchor=tk.CENTER)
        self.tree.column('score', width=140, anchor=tk.CENTER)

        self.tree.heading('user_id', text='ID')
        self.tree.heading('name', text='Имя игрока')
        self.tree.heading('sex', text='Пол игрока')
        self.tree.heading('old', text='Возраст игрока')
        self.tree.heading('score', text='Результат игрока')

        self.tree.pack()

    def open_dialog(self):
        Child(self)


class DB:
    with sq.connect('BD/saper.db') as con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS users")
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sexINTEGER NOT NULL DEFAULT 1,
        oldINTEGER,
        scoreINTEGER
        )""")

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Работа с базой данных Сапер")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()

