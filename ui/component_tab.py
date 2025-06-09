import tkinter as tk
from tkinter import ttk


class ComponentTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None

        self.comp_id = tk.IntVar()
        self.name = tk.StringVar()
        self.unit = tk.StringVar()
        self.quantity = tk.IntVar(value=0)

        ttk.Label(self, text="Name").grid(row=0, column=0, sticky="e")
        ttk.Entry(self, textvariable=self.name).grid(row=0, column=1, sticky="ew")

        ttk.Label(self, text="Unit").grid(row=1, column=0, sticky="e")
        self.unit_cb = ttk.Combobox(self, textvariable=self.unit, state="readonly",
                                    values=("pcs", "kg", "m"))
        self.unit_cb.grid(row=1, column=1, sticky="ew")

        ttk.Label(self, text="Qty").grid(row=2, column=0, sticky="e")
        self.qty_sp = tk.Spinbox(self, from_=0, to=100000, textvariable=self.quantity)
        self.qty_sp.grid(row=2, column=1, sticky="ew")

        self.btn_add = ttk.Button(self, text="Add")
        self.btn_update = ttk.Button(self, text="Update")
        self.btn_delete = ttk.Button(self, text="Delete")
        self.btn_add.grid(row=3, column=0, pady=4)
        self.btn_update.grid(row=3, column=1, pady=4)
        self.btn_delete.grid(row=3, column=2, pady=4)

        columns = ("name", "unit", "qty")
        self.table = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.table.heading(col, text=col.title())

        scroll = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scroll.set)

        self.table.grid(row=4, column=0, columnspan=3, sticky="nsew")
        scroll.grid(row=4, column=3, sticky="ns")

        self.columnconfigure(1, weight=1)
        self.rowconfigure(4, weight=1)

    def set_controller(self, ctrl):
        self.controller = ctrl
        if ctrl is None:
            return
        if hasattr(ctrl, "on_add"):
            self.btn_add.config(command=ctrl.on_add)
        if hasattr(ctrl, "on_update"):
            self.btn_update.config(command=ctrl.on_update)
        if hasattr(ctrl, "on_delete"):
            self.btn_delete.config(command=ctrl.on_delete)

    def dto_from_form(self):
        return {
            "name": self.name.get(),
            "unit": self.unit.get(),
            "quantity_in_stock": self.quantity.get(),
        }

    def refresh(self, data):
        for item in self.table.get_children():
            self.table.delete(item)
        for row in data:
            self.table.insert(
                "",
                "end",
                iid=row.get("id"),
                values=(
                    row.get("name"),
                    row.get("unit"),
                    row.get("quantity_in_stock"),
                ),
            )

    def clear_form(self):
        self.comp_id.set(0)
        self.name.set("")
        self.unit.set("")
        self.quantity.set(0)
        if self.unit_cb["values"]:
            self.unit_cb.set("")
        self.qty_sp.delete(0, tk.END)
        self.qty_sp.insert(0, "0")
