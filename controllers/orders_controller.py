class OrderController:
    def __init__(self, service=None, view=None, contract_service=None):
        self.service = service
        self.view = view
        self.contract_service = contract_service

    def create_order(self):
        """Create an order from the view form."""
        if not self.view or not self.service:
            return
        dto = {}
        if hasattr(self.view, "dto_from_form"):
            dto = self.view.dto_from_form()
        self.service.create(dto)
        if hasattr(self.view, "refresh"):
            self.view.refresh(self.service.list_all())

    def check_contract(self):
        """Validate selected supplier contract."""
        if not self.contract_service or not self.view:
            return None
        cid = None
        if hasattr(self.view, "get_selected_contract"):
            cid = self.view.get_selected_contract()
        return self.contract_service.verify(cid)
