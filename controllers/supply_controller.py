class SupplyController:
    def __init__(self, service=None, view=None):
        self.service = service
        self.view = view

    def register_supply(self):
        """Register a new supply."""
        if not self.view or not self.service:
            return
        # Expect view to provide get_supply() and get_records() helpers
        if hasattr(self.view, "get_supply") and hasattr(self.view, "get_records"):
            supply = self.view.get_supply()
            records = self.view.get_records()
            self.service.register_supply(supply, records)
        else:
            # Fallback: try to read minimal fields directly
            try:
                supply = self.view.supply
                records = self.view.records
                self.service.register_supply(supply, records)
            except AttributeError:
                # Not enough information – ignore in stub implementation
                pass
