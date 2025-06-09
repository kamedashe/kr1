from dao.supply_dao import SupplyDAO

class HistoryService:
    def __init__(self, history_dao):
        self.history_dao = history_dao

    def get_history(self, filters=None):
        """Return supply history records from DAO."""
        return self.history_dao.fetch_records(filters)

