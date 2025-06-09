class ReportController:
    def __init__(self, report_service=None, history_service=None, view=None):
        self.report_service = report_service
        self.history_service = history_service
        self.view = view

    def generate_report(self):
        """Fetch history and export to a chosen file."""
        if not self.report_service or not self.history_service:
            return
        rows = self.history_service.list_all()
        if not rows:
            return
        from tkinter.filedialog import asksaveasfilename
        path = asksaveasfilename()
        if not path:
            return
        kind = "pdf" if path.lower().endswith(".pdf") else "csv"
        return self.report_service.export(kind, rows, path)

    def show_supply_history(self):
        """Refresh the view with supply history."""
        if not self.history_service or not self.view:
            return
        if hasattr(self.view, "refresh"):
            self.view.refresh(self.history_service.list_all())
