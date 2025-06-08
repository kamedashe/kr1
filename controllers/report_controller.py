class ReportController:
    def __init__(self, report_service=None, history_service=None, view=None):
        self.report_service = report_service
        self.history_service = history_service
        self.view = view

    def generate_report(self):
        """Generate a report using the configured service."""
        pass

    def show_supply_history(self):
        """Display supply history using the history service."""
        pass
