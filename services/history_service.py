class HistoryService:
    def __init__(self, history_dao):
        self.history_dao = history_dao

    def get_history(self, filters=None):
        """Return supply history records from DAO."""
        if hasattr(self.history_dao, "fetch_records"):
            return self.history_dao.fetch_records(filters)
        return self.history_dao.select_all()

    def list_all(self):
        return self.history_dao.select_all()
