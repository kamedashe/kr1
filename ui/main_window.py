import tkinter as tk
from tkinter import ttk

from ui.reports_tab import ReportsTab
from ui.suppliers_tab import SuppliersTab
from ui.orders_tab import OrdersTab
from ui.warehouse_tab import WarehouseTab
from ui.component_tab import ComponentTab
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

        self.nb = ttk.Notebook(self)
        self.nb.grid(row=0, column=0, sticky="nsew")
        self.nb.rowconfigure(0, weight=1)
        self.nb.columnconfigure(0, weight=1)

        tabs = [
            ("Звіти", ReportsTab(self.nb)),
            ("Постачальники", SuppliersTab(self.nb)),
            ("Замовлення", OrdersTab(self.nb)),
            ("Склади", WarehouseTab(self.nb)),
            ("Комплектуючі", ComponentTab(self.nb)),
            ("Комірники", StorekeeperTab(self.nb)),
            ("Поставки", SupplyTab(self.nb)),
        ]

        for text, tab in tabs:
            self.nb.add(tab, text=text)



        self.reports_controller = None
        self.suppliers_controller = None
        self.orders_controller = None
        self.warehouse_controller = None

    def set_reports_controller(self, ctrl):
        self.reports_controller = ctrl

    def set_suppliers_controller(self, ctrl):
        self.suppliers_controller = ctrl

    def set_orders_controller(self, ctrl):
        self.orders_controller = ctrl

    def set_warehouse_controller(self, ctrl):
        self.warehouse_controller = ctrl


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()

