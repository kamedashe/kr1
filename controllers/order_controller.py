class OrderController:
    def __init__(self, service=None, view=None):
        self.service = service
        self.view = view

    def create_order(self):
        """Create a new order."""
        pass

    def check_contract(self):
        """Check supplier contract for the current order."""
        pass
