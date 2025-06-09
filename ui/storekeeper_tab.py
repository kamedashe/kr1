import tkinter as tk
from tkinter import ttk


class StorekeeperTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.ctrl = None

        ttk.Label(self, text="Component").grid(row=0, column=0, sticky="e")
        self.component_cb = ttk.Combobox(self, state="readonly")
        self.component_cb.grid(row=0, column=1, sticky="ew")

        ttk.Label(self, text="Quantity").grid(row=1, column=0, sticky="e")
        self.qty_sp = tk.Spinbox(self, from_=1, to=100000)
        self.qty_sp.grid(row=1, column=1, sticky="ew")

        self.btn_expense = ttk.Button(self, text="Register expense")
        self.btn_inventory = ttk.Button(self, text="Show inventory")

        self.btn_expense.grid(row=2, column=0, pady=4)
        self.btn_inventory.grid(row=2, column=1, pady=4)

        self.columnconfigure(1, weight=1)

    def set_controller(self, ctrl):
        self.ctrl = ctrl
        if ctrl is None:
            return
        if hasattr(ctrl, "register_expense"):
            self.btn_expense.config(command=ctrl.register_expense)
        if hasattr(ctrl, "show_inventory"):
            self.btn_inventory.config(command=ctrl.show_inventory)
