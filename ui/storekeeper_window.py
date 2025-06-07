import tkinter as tk
from tkinter import ttk, messagebox
from db.database import get_connection
from dao.storekeeper_dao import StorekeeperDAO
from dao.warehouse_dao import WarehouseDAO
from services.storekeeper_service import StorekeeperService
from services.warehouse_service import WarehouseService
from models.storekeeper import Storekeeper

class StorekeeperWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Комірники")
        self.center_window(400, 300)

        conn = get_connection()
        self.service = StorekeeperService(StorekeeperDAO(conn))
        self.warehouse_service = WarehouseService(WarehouseDAO(conn))
        self.warehouses = self.warehouse_service.list_all()

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True)

        tk.Label(self.frame, text="Ім’я:").grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(self.frame, text="Склад:").grid(row=1, column=0, sticky="e")
        self.wh_cb = ttk.Combobox(self.frame, state="readonly", width=40, values=[
            f"{w.id}: {w.name}" for w in self.warehouses
        ])
        self.wh_cb.grid(row=1, column=1, padx=5, pady=2)

        self.add_button = tk.Button(self.frame, text="Додати", width=12, command=self.add)
        self.add_button.grid(row=2, column=0, pady=5, padx=5)

        self.edit_button = tk.Button(self.frame, text="Редагувати", width=12, command=self.edit)
        self.edit_button.grid(row=2, column=1, pady=5, padx=5)

        self.delete_button = tk.Button(self.frame, text="Видалити", width=12, command=self.delete)
        self.delete_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.listbox = tk.Listbox(self.frame, width=50)
        self.listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=10)
        self.refresh()

    def center_window(self, width, height):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def add(self):
        name = self.name_entry.get().strip()
        wid_index = self.wh_cb.current()
        if not name or wid_index == -1:
            messagebox.showwarning("Помилка", "Вкажіть ім’я та оберіть склад.")
            return
        warehouse_id = self.warehouses[wid_index].id
        try:
            self.service.create(Storekeeper(name=name, warehouse_id=warehouse_id))
            self._clear_inputs()
            self.refresh()
        except ValueError as err:
            messagebox.showerror("Помилка", str(err))

    def edit(self):
        kid = self._selected_id()
        if kid is None:
            return
        k = self.service.get_by_id(kid)
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, k.name)
        for i, w in enumerate(self.warehouses):
            if w.id == k.warehouse_id:
                self.wh_cb.current(i)
                break
        self.add_button.config(text="Зберегти", command=lambda: self.save(k.id))

    def save(self, kid: int):
        name = self.name_entry.get().strip()
        wid_index = self.wh_cb.current()
        if not name or wid_index == -1:
            messagebox.showwarning("Помилка", "Вкажіть ім’я та оберіть склад.")
            return
        warehouse_id = self.warehouses[wid_index].id
        try:
            self.service.update(Storekeeper(id=kid, name=name, warehouse_id=warehouse_id))
        except ValueError as err:
            messagebox.showerror("Помилка", str(err))
            return
        self.add_button.config(text="Додати", command=self.add)
        self._clear_inputs()
        self.refresh()

    def delete(self):
        kid = self._selected_id()
        if kid is None:
            return
        if messagebox.askyesno("Підтвердження", "Видалити комірника?"):
            self.service.delete(kid)
            self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for k in self.service.list_all():
            self.listbox.insert(tk.END, f"{k.id}. {k.name} — склад {k.warehouse_id}")

    def _clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.wh_cb.set('')

    def _selected_id(self) -> int | None:
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Виберіть", "Оберіть елемент зі списку.")
            return None
        return int(self.listbox.get(sel[0]).split('.')[0])
