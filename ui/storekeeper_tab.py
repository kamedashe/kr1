from tkinter import ttk


class StorekeeperTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller: object | None = None

        self.btn_expense = ttk.Button(self, text="Реєструвати видатки")
        self.btn_view = ttk.Button(self, text="Переглянути інвентар")

        self.btn_expense.grid(row=0, column=0, padx=4, pady=4, sticky="w")
        self.btn_view.grid(row=0, column=1, padx=4, pady=4, sticky="w")

    def set_controller(self, ctrl):
        self.controller = ctrl
        if ctrl is None:
            return
        if hasattr(ctrl, "register_expense"):
            self.btn_expense.config(command=ctrl.register_expense)
        if hasattr(ctrl, "show_stock"):
            self.btn_view.config(command=ctrl.show_stock)

