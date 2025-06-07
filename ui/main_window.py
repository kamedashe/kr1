import tkinter as tk
from tkinter import ttk

from ui.component_tab import ComponentTab
from ui.supplier_tab import SupplierTab
from ui.warehouse_tab import WarehouseTab
from ui.storekeeper_tab import StorekeeperTab
from ui.supply_tab import SupplyTab


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ІС відділу комплектації")
        self.geometry("900x600")
        self.minsize(800, 500)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        notebook = ttk.Notebook(self)
        notebook.grid(row=0, column=0, sticky="nsew")
        notebook.rowconfigure(0, weight=1)
        notebook.columnconfigure(0, weight=1)

        tabs = [
            ("Комплектуючі", ComponentTab(notebook)),
            ("Постачальники", SupplierTab(notebook)),
            ("Склади", WarehouseTab(notebook)),
            ("Комірники", StorekeeperTab(notebook)),
            ("Поставки", SupplyTab(notebook)),
        ]

        for text, tab in tabs:
            notebook.add(tab, text=text)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
