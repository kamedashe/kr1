import tkinter as tk
from tkinter import ttk


class SupplierTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None

        self.name = tk.StringVar()
        self.email = tk.StringVar()
        self.phone = tk.StringVar()

        ttk.Label(self, text="Name").grid(row=0, column=0, sticky="e")
        ttk.Entry(self, textvariable=self.name).grid(row=0, column=1, sticky="ew")
        ttk.Label(self, text="Email").grid(row=1, column=0, sticky="e")
        ttk.Entry(self, textvariable=self.email).grid(row=1, column=1, sticky="ew")
        ttk.Label(self, text="Phone").grid(row=2, column=0, sticky="e")
        ttk.Entry(self, textvariable=self.phone).grid(row=2, column=1, sticky="ew")

        self.btn_add = ttk.Button(self, text="Add")
        self.btn_update = ttk.Button(self, text="Update")
        self.btn_delete = ttk.Button(self, text="Delete")

        self.btn_add.grid(row=3, column=0, pady=4)
        self.btn_update.grid(row=3, column=1, pady=4)
        self.btn_delete.grid(row=3, column=2, pady=4)

        columns = ("name", "email", "phone")
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

    def refresh(self, data):
        for item in self.table.get_children():
            self.table.delete(item)
        for row in data:
            self.table.insert("", "end", iid=row.get("id"), values=(row.get("name"), row.get("email"), row.get("phone")))
