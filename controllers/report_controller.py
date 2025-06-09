class ReportController:
    def __init__(self, report_service=None, history_service=None, view=None):
        self.report_service = report_service
        self.history_service = history_service
        self.view = view

    def generate_report(self):
        """Generate a report using the configured service."""
        if not self.report_service or not self.view:
            return
        rows = []
        if hasattr(self.view, "get_rows"):
            rows = self.view.get_rows()
        out = self.report_service.export(rows, "report.out")
        return out

    def show_supply_history(self):
        """Display supply history using the history service."""
        if not self.history_service or not self.view:
            return
        data = self.history_service.get_history()
        if hasattr(self.view, "display_history"):
            self.view.display_history(data)
