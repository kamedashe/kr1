
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

from db.database import get_connection
from dao.component_dao import ComponentDAO
from dao.warehouse_dao import WarehouseDAO
from dao.supplier_dao import SupplierDAO
from dao.storekeeper_dao import StorekeeperDAO
from dao.supply_dao import SupplyDAO
from dao.supply_record_dao import SupplyRecordDAO
from services.component_service import ComponentService
from services.warehouse_service import WarehouseService
from services.supplier_service import SupplierService
from services.storekeeper_service import StorekeeperService
from services.supply_service import SupplyService
from services.inventory_observer import InventoryObserver
from models.supply import Supply
from models.supply_record import SupplyRecord

class SupplyWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Нова поставка")
        self.center_window(400, 300)

        conn = get_connection()
        # Service layer
        self.component_service   = ComponentService(ComponentDAO(conn))
        self.warehouse_service   = WarehouseService(WarehouseDAO(conn))
        self.supplier_service    = SupplierService(SupplierDAO(conn))
        self.storekeeper_service = StorekeeperService(StorekeeperDAO(conn))
        self.supply_service      = SupplyService(
            SupplyDAO(conn),
            SupplyRecordDAO(conn, InventoryObserver(ComponentDAO(conn)))
        )

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True)

        self.suppliers   = self.supplier_service.list_all()
        self.warehouses  = self.warehouse_service.list_all()
        self.storekeepers= self.storekeeper_service.list_all()
        self.components  = self.component_service.list_all()

        # --- Основна форма ---
        self.supplier_cb   = self._cb("Постачальник:", [f"{s.id}: {s.name}" for s in self.suppliers], 0)
        self.warehouse_cb  = self._cb("Склад:",        [f"{w.id}: {w.name}" for w in self.warehouses], 1)
        self.storekeeper_cb= self._cb("Комірник:",     [f"{k.id}: {k.name}" for k in self.storekeepers], 2)

        # --- Позиції ---
        self.component_cb = self._cb("Компонент:", [f"{c.id}: {c.name}" for c in self.components], 3)
        tk.Label(self.frame, text="Кількість:").grid(row=4, column=0, sticky="e")
        self.qty_entry = tk.Entry(self.frame)
        self.qty_entry.grid(row=4, column=1)
        tk.Label(self.frame, text="Ціна за од.").grid(row=5, column=0, sticky="e")
        self.price_entry = tk.Entry(self.frame)
        self.price_entry.grid(row=5, column=1)

        tk.Button(self.frame, text="Додати позицію", command=self.add_record).grid(row=6, column=0, columnspan=2, pady=5)

        self.items_listbox = tk.Listbox(self.frame, width=60)
        self.items_listbox.grid(row=7, column=0, columnspan=2, pady=5)

        tk.Button(self.frame, text="Оформити поставку", command=self.submit).grid(row=8, column=0, columnspan=2, pady=10)

        self.records: list[SupplyRecord] = []

    # --------------------- helpers -------------------------------
    def _cb(self, label, values, row):
        tk.Label(self.frame, text=label).grid(row=row, column=0, sticky="e")
        cb = ttk.Combobox(self.frame, state="readonly", values=values)
        cb.grid(row=row, column=1)
        return cb

    
    def center_window(self, width, height):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    # --------------------- add record ----------------------------
    def add_record(self):
        idx = self.component_cb.current()
        qty = self.qty_entry.get()
        price= self.price_entry.get()
        if idx == -1 or not qty or not price:
            messagebox.showwarning("Помилка", "Заповніть усі поля.")
            return
        try:
            quantity = int(qty)
            unit_price = float(price)
        except ValueError:
            messagebox.showerror("Помилка", "Кількість – ціле, ціна – число.")
            return
        comp_id = self.components[idx].id
        rec = SupplyRecord(supply_id=None, component_id=comp_id, quantity=quantity, price=unit_price)
        self.records.append(rec)
        self.items_listbox.insert(tk.END, f"{self.components[idx].name} x{quantity} @ {unit_price}")
        self.qty_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    # --------------------- submit supply -------------------------
    def submit(self):
        sup_i = self.supplier_cb.current()
        wh_i  = self.warehouse_cb.current()
        sk_i  = self.storekeeper_cb.current()
        if -1 in (sup_i, wh_i, sk_i) or not self.records:
            messagebox.showwarning("Помилка", "Заповніть усі поля та додайте позиції.")
            return
        supply = Supply(
            supply_date=date.today(),
            supplier_id   = self.suppliers[sup_i].id,
            warehouse_id  = self.warehouses[wh_i].id,
            storekeeper_id= self.storekeepers[sk_i].id
        )
        try:
            self.supply_service.register_supply(supply, self.records)
        except ValueError as err:
            messagebox.showerror("Помилка", str(err))
            return
        messagebox.showinfo("Успіх", "Поставка зареєстрована!")
        # reset state
        self.records.clear()
        self.items_listbox.delete(0, tk.END)
