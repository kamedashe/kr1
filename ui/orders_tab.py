from tkinter import ttk


class OrdersTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.ctrl = None

        self.btn_create = ttk.Button(self, text="Формувати замовлення")
        self.btn_check = ttk.Button(self, text="Перевірити контракт")
        self.btn_create.grid(row=0, column=0, sticky="w", pady=4, padx=4)
        self.btn_check.grid(row=1, column=0, sticky="w", pady=4, padx=4)

        columns = ("order_id", "supplier", "status", "date")
        self.table = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.table.heading(col, text=col.title())

        scroll = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scroll.set)

        self.table.grid(row=2, column=0, sticky="nsew")
        scroll.grid(row=2, column=1, sticky="ns")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

    def set_controller(self, ctrl):
        self.ctrl = ctrl
        self.btn_create.config(command=self.ctrl.create_order)
        self.btn_check.config(command=self.ctrl.check_contract)

    def refresh(self, data):
        for item in self.table.get_children():
            self.table.delete(item)
        for row in data:
            self.table.insert(
                "",
                "end",
                iid=row.get("id"),
                values=(
                    row.get("order_id"),
                    row.get("supplier"),
                    row.get("status"),
                    row.get("date"),
                ),
            )

