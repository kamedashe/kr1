import tkinter as tk
from tkinter import messagebox
from db.database import get_connection
from dao.warehouse_dao import WarehouseDAO
from services.warehouse_service import WarehouseService
from models.warehouse import Warehouse

class WarehouseWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Склади")
        self.center_window(400, 300)

        conn = get_connection()
        self.service = WarehouseService(WarehouseDAO(conn))

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True)


        tk.Label(self.frame, text="Назва:").grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(self.frame, text="Локація:").grid(row=1, column=0, sticky="e")
        self.loc_entry = tk.Entry(self.frame)
        self.loc_entry.grid(row=1, column=1, padx=5, pady=2)

        self.add_button = tk.Button(self.frame, text="Додати", width=12, command=self.add)
        self.add_button.grid(row=2, column=0, pady=5, padx=5)
        self.edit_button = tk.Button(self.frame, text="Редагувати", width=12, command=self.edit)
        self.edit_button.grid(row=2, column=1, pady=5, padx=5)
        self.delete_button = tk.Button(self.frame, text="Видалити", width=12, command=self.delete)
        self.delete_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.listbox = tk.Listbox(self.frame, width=50)
        self.listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=10)
        self.refresh()
        
    def center_window(self, width=400, height=300):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def add(self):
        name = self.name_entry.get().strip()
        loc  = self.loc_entry.get().strip()
        if not name:
            messagebox.showwarning("Помилка", "Назва не може бути порожньою.")
            return
        try:
            self.service.create(Warehouse(name=name, location=loc))
            self._clear_inputs()
            self.refresh()
        except ValueError as err:
            messagebox.showerror("Помилка", str(err))

    def edit(self):
        wid = self._selected_id()
        if wid is None:
            return
        w = self.service.get_by_id(wid)
        self.name_entry.delete(0, tk.END)
        self.loc_entry.delete(0, tk.END)
        self.name_entry.insert(0, w.name)
        self.loc_entry.insert(0, w.location or "")
        self.add_button.config(text="Зберегти", command=lambda: self.save(wid))

    def save(self, wid: int):
        name = self.name_entry.get().strip()
        loc  = self.loc_entry.get().strip()
        try:
            self.service.update(Warehouse(id=wid, name=name, location=loc))
        except ValueError as err:
            messagebox.showerror("Помилка", str(err))
            return
        self.add_button.config(text="Додати", command=self.add)
        self._clear_inputs()
        self.refresh()

    def delete(self):
        wid = self._selected_id()
        if wid is None:
            return
        if messagebox.askyesno("Підтвердження", "Видалити склад?"):
            self.service.delete(wid)
            self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for w in self.service.list_all():
            self.listbox.insert(tk.END, f"{w.id}. {w.name} — {w.location}")

    def _clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.loc_entry.delete(0, tk.END)

    def _selected_id(self) -> int | None:
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Виберіть", "Оберіть елемент зі списку.")
            return None
        return int(self.listbox.get(sel[0]).split('.')[0])
