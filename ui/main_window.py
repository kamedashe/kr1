import tkinter as tk
from tkinter import ttk


class ComponentTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


class SupplierTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


class WarehouseTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


class StorekeeperTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


class SupplyTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


class MainWindow(ttk.Frame):
    def __init__(self, root: tk.Tk):
        super().__init__(root)
        root.title("ІС відділу комплектації")
        root.geometry("900x600")
        root.minsize(800, 500)
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)

        self.grid(row=0, column=0, sticky="nsew")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        notebook = ttk.Notebook(self)
        notebook.grid(row=0, column=0, sticky="nsew")

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
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()
