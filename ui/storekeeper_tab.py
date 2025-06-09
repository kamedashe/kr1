from tkinter import ttk


class StorekeeperTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None

        self.btn_register = ttk.Button(self, text="Реєструвати видатки")
        self.btn_view = ttk.Button(self, text="Переглянути інвентар")

        self.btn_register.grid(row=0, column=0, pady=4, padx=4, sticky="w")
        self.btn_view.grid(row=0, column=1, pady=4, padx=4, sticky="w")

    def set_controller(self, ctrl):
        self.controller = ctrl
        if hasattr(ctrl, "register_expense"):
            self.btn_register.config(command=ctrl.register_expense)
        if hasattr(ctrl, "view_inventory"):
            self.btn_view.config(command=ctrl.view_inventory)
