class SupplyController:
    def __init__(self, service=None, view=None):
        self.service = service
        self.view = view

    def register_supply(self):
        """Register supply via service and fire event."""
        if not self.service:
            return
        dto = {}
        if self.view and hasattr(self.view, "dto_from_form"):
            dto = self.view.dto_from_form()
        elif self.view:
            try:
                dto = {
                    "supply": self.view.get_supply(),
                    "records": self.view.get_records(),
                }
            except AttributeError:
                pass
        result = self.service.register(dto)
        if self.view and hasattr(self.view, "event_generate"):
            self.view.event_generate("<<SupplySaved>>")
        return result
