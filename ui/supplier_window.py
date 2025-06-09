import tkinter as tk
from tkinter import messagebox
from db.database import get_connection
from dao.supplier_dao import SupplierDAO
from services.supplier_service import SupplierService
from models.supplier import Supplier

class SupplierWindow:
    def __init__(self, root: tk.Toplevel | tk.Tk):
        self.root = root
        self.root.title("Постачальники")
        self.center_window(400, 300)

        conn = get_connection()
        self.service = SupplierService(SupplierDAO(conn))

        # Контейнер для всіх елементів
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        # Поля вводу
        tk.Label(self.frame, text="Назва:").grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(self.frame, text="Контакт:").grid(row=1, column=0, sticky="e")
        self.contact_entry = tk.Entry(self.frame)
        self.contact_entry.grid(row=1, column=1, padx=5, pady=2)

        # Кнопки
        self.add_button = tk.Button(self.frame, text="Додати", width=12, command=self.add)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)
        self.edit_button = tk.Button(self.frame, text="Редагувати", width=12, command=self.edit)
        self.edit_button.grid(row=2, column=1, padx=5, pady=5)
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
        contact = self.contact_entry.get().strip()
        if not name:
            messagebox.showwarning("Помилка", "Назва обовʼязкова")
            return
        try:
            self.service.create(Supplier(name=name, contact_info=contact))
            self._clear_inputs()
            self.refresh()
        except ValueError as err:
            messagebox.showerror("Помилка", str(err))

    def edit(self):
        sid = self._selected_id()
        if sid is None:
            return
        s = self.service.get_by_id(sid)
        self.name_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.name_entry.insert(0, s.name)
        self.contact_entry.insert(0, s.contact_info or "")
        self.add_button.config(text="Зберегти", command=lambda: self.save(sid))

    def save(self, sid: int):
        name = self.name_entry.get().strip()
        contact = self.contact_entry.get().strip()
        try:
            self.service.update(Supplier(id=sid, name=name, contact_info=contact))
        except ValueError as err:
            messagebox.showerror("Помилка", str(err))
            return
        self.add_button.config(text="Додати", command=self.add)
        self._clear_inputs()
        self.refresh()

    def delete(self):
        sid = self._selected_id()
        if sid is None:
            return
        if messagebox.askyesno("Підтвердження", "Видалити постачальника?"):
            self.service.delete(sid)
            self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for s in self.service.list_all():
            self.listbox.insert(tk.END, f"{s.id}. {s.name} | {s.contact_info or ''}")

    def _clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)

    def _selected_id(self) -> int | None:
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Виберіть", "Оберіть елемент зі списку.")
            return None
        return int(self.listbox.get(sel[0]).split('.')[0])
