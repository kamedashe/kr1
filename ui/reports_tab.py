diff --git a//dev/null b/ui/reports_tab.py
index 0000000000000000000000000000000000000000..fffc670c29f3d8b20fe69d8e53b6a133f6257f3d 100644
--- a//dev/null
+++ b/ui/reports_tab.py
@@ -0,0 +1,21 @@
+from tkinter import ttk
+
+
+class ReportsTab(ttk.Frame):
+    def __init__(self, parent):
+        super().__init__(parent)
+        self.ctrl = None
+
+        self.btn_report = ttk.Button(self, text="Формувати звіт")
+        self.btn_history = ttk.Button(self, text="Історія постачань")
+
+        self.btn_report.grid(row=0, column=0, pady=4, padx=4)
+        self.btn_history.grid(row=1, column=0, pady=4, padx=4)
+
+    def set_controller(self, ctrl):
+        self.ctrl = ctrl
+        self.btn_report.config(command=self.ctrl.generate_report)
+        self.btn_history.config(command=self.ctrl.show_supply_history)
+
+    def refresh(self, data):
+        pass
