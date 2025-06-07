from tkinter import ttk


class ReportsTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.ctrl = None

        self.btn_report = ttk.Button(self, text="Формувати звіт")
        self.btn_history = ttk.Button(self, text="Історія постачань")

        self.btn_report.grid(row=0, column=0, pady=4, padx=4)
        self.btn_history.grid(row=1, column=0, pady=4, padx=4)

    def set_controller(self, ctrl):
        self.ctrl = ctrl
        self.btn_report.config(command=self.ctrl.generate_report)
        self.btn_history.config(command=self.ctrl.show_supply_history)

    def refresh(self, data):
        pass
