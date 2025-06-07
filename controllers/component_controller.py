diff --git a//dev/null b/controllers/component_controller.py
index 0000000000000000000000000000000000000000..ca706329095a217dbf0dadb3ed233c680e2680e7 100644
--- a//dev/null
+++ b/controllers/component_controller.py
@@ -0,0 +1,34 @@
+from services.component_service import ComponentService
+from ui.component_tab import ComponentTab
+
+
+class ComponentController:
+    def __init__(self, service: ComponentService, view: ComponentTab):
+        self.service = service
+        self.view = view
+        view.btn_add.config(command=self.on_add)
+        view.btn_update.config(command=self.on_update)
+        view.btn_delete.config(command=self.on_delete)
+
+    def _dto_from_view(self) -> dict:
+        return {
+            "name": self.view.name.get(),
+            "unit": self.view.unit.get(),
+            "qty": self.view.quantity.get(),
+        }
+
+    def on_add(self):
+        dto = self._dto_from_view()
+        self.service.create(dto)
+        self.view.refresh(self.service.list_all())
+
+    def on_update(self):
+        cid = self.view.comp_id.get()
+        dto = self._dto_from_view()
+        self.service.update(cid, dto)
+        self.view.refresh(self.service.list_all())
+
+    def on_delete(self):
+        cid = self.view.comp_id.get()
+        self.service.delete(cid)
+        self.view.refresh(self.service.list_all())
