from dao.supply_dao import SupplyDAO
from dao.supply_record_dao import SupplyRecordDAO
from models.supply import Supply
from models.supply_record import SupplyRecord

class SupplyService:
    """Реєстрація поставок з формуванням події."""

    def __init__(self, supply_dao: SupplyDAO, record_dao: SupplyRecordDAO):
        self.supply_dao = supply_dao
        self.record_dao = record_dao

    def register(self, dto: dict) -> str:
        supply: Supply = dto.get("supply")
        records: list[SupplyRecord] = dto.get("records", [])
        self.register_supply(supply, records)
        return "<<SupplySaved>>"

    def register_supply(self, supply: Supply, records: list[SupplyRecord]) -> Supply:
        if not records:
            raise ValueError("Supply must contain at least one record")
        self.supply_dao.insert(supply)  # заповнює supply.id
        for rec in records:
            rec.supply_id = supply.id
            self.record_dao.insert(rec)  # Observer збільшить залишки
        return supply