from tkinter import ttk


class WarehouseTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.ctrl = None

        self.btn_show = ttk.Button(self, text="Переглянути залишки")
        self.btn_expense = ttk.Button(self, text="Реєструвати видатки")
        self.btn_supply = ttk.Button(self, text="Реєструвати постачання")

        self.btn_show.grid(row=0, column=0, sticky="w", padx=4, pady=4)
        self.btn_expense.grid(row=1, column=0, sticky="w", padx=4, pady=4)
        self.btn_supply.grid(row=2, column=0, sticky="w", padx=4, pady=4)

        columns = ("component", "qty", "unit")
        self.table = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.table.heading(col, text=col.title())
        scroll = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scroll.set)

        self.table.grid(row=3, column=0, sticky="nsew")
        scroll.grid(row=3, column=1, sticky="ns")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)

    def set_controller(self, ctrl):
        self.ctrl = ctrl
        self.btn_show.config(command=self.ctrl.show_stock)
        self.btn_expense.config(command=self.ctrl.register_expense)
        self.btn_supply.config(command=self.ctrl.register_supply)

    def refresh(self, data):
        for item in self.table.get_children():
            self.table.delete(item)
        for row in data:
            self.table.insert(
                "",
                "end",
                iid=row.get("id"),
                values=(row.get("component"), row.get("qty"), row.get("unit")),
            )
