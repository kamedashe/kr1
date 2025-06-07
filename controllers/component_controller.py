from services.component_service import ComponentService
from ui.component_tab import ComponentTab


class ComponentController:
    def __init__(self, service: ComponentService, view: ComponentTab):
        self.service = service
        self.view = view
        view.btn_add.config(command=self.on_add)
        view.btn_update.config(command=self.on_update)
        view.btn_delete.config(command=self.on_delete)

    def _dto_from_view(self) -> dict:
        return {
            "id": self.view.comp_id.get(),
            "name": self.view.name.get(),
            "unit": self.view.unit.get(),
            "quantity_in_stock": self.view.quantity.get(),
        }

    def on_add(self):
        dto = self._dto_from_view()
        self.service.create(dto)
        self.view.refresh(self.service.list_all())

    def on_update(self):
        dto = self._dto_from_view()
        self.service.update(dto)
        self.view.refresh(self.service.list_all())

    def on_delete(self):
        cid = self.view.comp_id.get()
        self.service.delete(cid)
        self.view.refresh(self.service.list_all())
