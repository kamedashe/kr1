class SupplyController:
    def __init__(self, service=None, view=None):
        self.service = service
        self.view = view

    def register_supply(self):
        """Register supply via service."""
        if not self.view or not self.service:
            return
        dto = {}
        if hasattr(self.view, "dto_from_form"):
            dto = self.view.dto_from_form()
        else:
            try:
                dto = {
                    "supply": self.view.get_supply(),
                    "records": self.view.get_records(),
                }
            except AttributeError:
                return
        return self.service.register(dto)
