import tkinter as tk
from tkinter import ttk


class SupplyTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.ctrl = None

        ttk.Label(self, text="Supplier").grid(row=0, column=0, sticky="e")
        self.supplier_cb = ttk.Combobox(self, state="readonly")
        self.supplier_cb.grid(row=0, column=1, sticky="ew")

        ttk.Label(self, text="Component").grid(row=1, column=0, sticky="e")
        self.component_cb = ttk.Combobox(self, state="readonly")
        self.component_cb.grid(row=1, column=1, sticky="ew")

        ttk.Label(self, text="Qty").grid(row=2, column=0, sticky="e")
        self.qty_sp = tk.Spinbox(self, from_=1, to=100000)
        self.qty_sp.grid(row=2, column=1, sticky="ew")

        ttk.Label(self, text="Date").grid(row=3, column=0, sticky="e")
        self.date_entry = ttk.Entry(self)
        self.date_entry.grid(row=3, column=1, sticky="ew")

        self.btn_register = ttk.Button(self, text="Зареєструвати постачання")
        self.btn_register.grid(row=4, column=0, columnspan=2, pady=4)

        columns = ("supplier", "component", "qty", "date")
        self.table = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.table.heading(col, text=col.title())

        scroll = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scroll.set)

        self.table.grid(row=5, column=0, columnspan=2, sticky="nsew")
        scroll.grid(row=5, column=2, sticky="ns")

        self.columnconfigure(1, weight=1)
        self.rowconfigure(5, weight=1)

    def set_controller(self, ctrl):
        self.ctrl = ctrl
        self.btn_register.config(command=self._on_register)

    def _on_register(self):
        if self.ctrl:
            self.ctrl.register_supply()
            self.event_generate("<<SupplySaved>>")

    def refresh(self, data):
        for item in self.table.get_children():
            self.table.delete(item)
        for row in data:
            self.table.insert(
                "",
                "end",
                iid=row.get("id"),
                values=(
                    row.get("supplier"),
                    row.get("component"),
                    row.get("qty"),
                    row.get("date"),
                ),
            )
