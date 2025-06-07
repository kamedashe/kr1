import tkinter as tk
from ui.component_window import ComponentWindow
from ui.warehouse_window import WarehouseWindow
from ui.storekeeper_window import StorekeeperWindow
from ui.supplier_window import SupplierWindow
from ui.supply_window import SupplyWindow
from tkinter import Tk
from ui.export_ui import create_export_ui

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Інформаційна система — Відділ комплектації")
        self.center_window(400, 300)

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True)

        btn = lambda txt, cmd: tk.Button(self.frame, text=txt, width=20, command=cmd)
        btn("Комплектуючі", self.open_components).pack(pady=5)
        btn("Постачальники", self.open_suppliers).pack(pady=5)
        btn("Склади", self.open_warehouses).pack(pady=5)
        btn("Комірники", self.open_storekeepers).pack(pady=5)
        btn("Нова поставка", self.open_supply).pack(pady=5)
        report_cb, btn_csv, btn_pdf = create_export_ui(root)


    def center_window(self, width, height):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def open_components(self):
        win = tk.Toplevel(self.root)
        ComponentWindow(win)

    def open_suppliers(self):
        win = tk.Toplevel(self.root)
        SupplierWindow(win)

    def open_warehouses(self):
        win = tk.Toplevel(self.root)
        WarehouseWindow(win)

    def open_storekeepers(self):
        win = tk.Toplevel(self.root)
        StorekeeperWindow(win)

    def get_table_data():
        columns = ['ID', 'Назва', 'Ціна']
        rows = [
            [1, 'Товар 1', 100],
            [2, 'Товар 2', 200],
            [3, 'Товар 3', 300],
        ]
        return rows, columns

    def open_supply(self):
        win = tk.Toplevel(self.root)
        SupplyWindow(win)

if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()
