import tkinter as tk
from tkinter import ttk

from ui.main_window import MainWindow

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Вхід")
        self.geometry("300x150")
        self.resizable(False, False)

        ttk.Label(self, text="Оберіть роль:").pack(pady=10)
        self.role_cb = ttk.Combobox(
            self,
            state="readonly",
            values=["Керівник", "Менеджер", "Склад"],
        )
        self.role_cb.pack(pady=5)
        ttk.Button(self, text="Увійти", command=self._login).pack(pady=10)

    def _login(self):
        role = self.role_cb.get()
        if not role:
            return
        self.destroy()
        main = MainWindow()
        nb = main.nb
        if role == "Керівник":
            nb.hide(nb.index("Постачальники"))
            nb.hide(nb.index("Замовлення"))
            nb.hide(nb.index("Склад"))
        elif role == "Менеджер":
            nb.hide(nb.index("Звіти"))
            nb.hide(nb.index("Склад"))
        elif role == "Склад":
            nb.hide(nb.index("Звіти"))
            nb.hide(nb.index("Постачальники"))
            nb.hide(nb.index("Замовлення"))
        main.mainloop()
