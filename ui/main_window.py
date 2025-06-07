diff --git a/ui/main_window.py b/ui/main_window.py
index 66ad01d96d7bfda856eb47ee05bdef0f895a60bc..ec5dcc724d22bb14361a509fd54b9a1d5ffad491 100644
--- a/ui/main_window.py
+++ b/ui/main_window.py
@@ -1,66 +1,49 @@
-import tkinter as tk
-from ui.component_window import ComponentWindow
-from ui.warehouse_window import WarehouseWindow
-from ui.storekeeper_window import StorekeeperWindow
-from ui.supplier_window import SupplierWindow
-from ui.supply_window import SupplyWindow
-from tkinter import Tk
-from ui.export_ui import create_export_ui
-
-class MainWindow:
-    def __init__(self, root):
-        self.root = root
-        self.root.title("Інформаційна система — Відділ комплектації")
-        self.center_window(400, 300)
-
-        self.frame = tk.Frame(self.root)
-        self.frame.pack(expand=True)
-
-        btn = lambda txt, cmd: tk.Button(self.frame, text=txt, width=20, command=cmd)
-        btn("Комплектуючі", self.open_components).pack(pady=5)
-        btn("Постачальники", self.open_suppliers).pack(pady=5)
-        btn("Склади", self.open_warehouses).pack(pady=5)
-        btn("Комірники", self.open_storekeepers).pack(pady=5)
-        btn("Нова поставка", self.open_supply).pack(pady=5)
-        report_cb, btn_csv, btn_pdf = create_export_ui(root)
-
-
-    def center_window(self, width, height):
-        self.root.update_idletasks()
-        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
-        y = (self.root.winfo_screenheight() // 2) - (height // 2)
-        self.root.geometry(f'{width}x{height}+{x}+{y}')
-
-    def open_components(self):
-        win = tk.Toplevel(self.root)
-        ComponentWindow(win)
-
-    def open_suppliers(self):
-        win = tk.Toplevel(self.root)
-        SupplierWindow(win)
-
-    def open_warehouses(self):
-        win = tk.Toplevel(self.root)
-        WarehouseWindow(win)
-
-    def open_storekeepers(self):
-        win = tk.Toplevel(self.root)
-        StorekeeperWindow(win)
-
-    def get_table_data():
-        columns = ['ID', 'Назва', 'Ціна']
-        rows = [
-            [1, 'Товар 1', 100],
-            [2, 'Товар 2', 200],
-            [3, 'Товар 3', 300],
-        ]
-        return rows, columns
-
-    def open_supply(self):
-        win = tk.Toplevel(self.root)
-        SupplyWindow(win)
-
-if __name__ == "__main__":
-    root = tk.Tk()
-    MainWindow(root)
-    root.mainloop()
+import tkinter as tk
+from tkinter import ttk
+
+from ui.reports_tab import ReportsTab
+from ui.suppliers_tab import SuppliersTab
+from ui.orders_tab import OrdersTab
+from ui.warehouse_tab import WarehouseTab
+
+
+class MainWindow(tk.Tk):
+    def __init__(self):
+        super().__init__()
+        self.title("ІС відділу комплектації")
+        self.geometry("900x600")
+        self.minsize(800, 500)
+        self.rowconfigure(0, weight=1)
+        self.columnconfigure(0, weight=1)
+
+        notebook = ttk.Notebook(self)
+        notebook.grid(row=0, column=0, sticky="nsew")
+        notebook.rowconfigure(0, weight=1)
+        notebook.columnconfigure(0, weight=1)
+
+        tabs = [
+            ("Звіти", ReportsTab(notebook)),
+            ("Постачальники", SuppliersTab(notebook)),
+            ("Замовлення", OrdersTab(notebook)),
+            ("Склади", WarehouseTab(notebook)),
+        ]
+
+        for text, tab in tabs:
+            notebook.add(tab, text=text)
+
+        self.reports_controller = None
+        self.suppliers_controller = None
+        self.orders_controller = None
+        self.warehouse_controller = None
+
+    def set_reports_controller(self, ctrl):
+        self.reports_controller = ctrl
+
+    def set_suppliers_controller(self, ctrl):
+        self.suppliers_controller = ctrl
+
+    def set_orders_controller(self, ctrl):
+        self.orders_controller = ctrl
+
+    def set_warehouse_controller(self, ctrl):
+        self.warehouse_controller = ctrl
