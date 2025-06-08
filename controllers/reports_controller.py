from services.report_service import ReportService
from services.history_service import HistoryService
from ui.reports_tab import ReportsTab
from ui.supply_history_window import SupplyHistoryWindow


class ReportsController:
    def __init__(self, view: ReportsTab, service: ReportService, history_service: HistoryService):
        self.view = view
        self.service = service
        self.history_service = history_service
        view.set_controller(self)

    def generate_report(self):
        self.service.create_report()

    def show_supply_history(self):
        data = self.history_service.list()
        SupplyHistoryWindow(data)
