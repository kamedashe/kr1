from services.supplier_service import SupplierService
from ui.supplier_tab import SupplierTab


class SupplierController:
    def __init__(self, service: SupplierService, view: SupplierTab):
        self.service = service
        self.view = view
        view.btn_add.config(command=self.on_add)
        view.btn_update.config(command=self.on_update)
        view.btn_delete.config(command=self.on_delete)

    def _dto_from_view(self) -> dict:
        return {
            "name": self.view.name.get(),
            "email": self.view.email.get(),
            "phone": self.view.phone.get(),
        }

    def _selected_id(self) -> int | None:
        sel = self.view.table.selection()
        if not sel:
            return None
        return int(sel[0])

    def on_add(self):
        self.service.create(self._dto_from_view())
        self.view.refresh(self.service.list_all())

    def on_update(self):
        sid = self._selected_id()
        if sid is None:
            return
        self.service.update(sid, self._dto_from_view())
        self.view.refresh(self.service.list_all())

    def on_delete(self):
        sid = self._selected_id()
        if sid is None:
            return
        self.service.delete(sid)
        self.view.refresh(self.service.list_all())
