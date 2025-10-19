from datetime import datetime

from ..dao.supply_dao import SupplyDAO
from ..dao.supply_record_dao import SupplyRecordDAO
from ..models.supply import Supply
from ..models.supply_record import SupplyRecord


class SupplyService:
    """Service for registering supplies with automatic inventory updates."""

    def __init__(self, supply_dao: SupplyDAO, record_dao: SupplyRecordDAO):
        self.supply_dao = supply_dao
        self.record_dao = record_dao

    def register(self, dto: dict) -> str:
        """Register a supply from dictionary data.

        Args:
            dto: Dictionary with 'supply' and 'records' keys.

        Returns:
            Success message.
        """
        supply: Supply = dto.get("supply")
        records: list[SupplyRecord] = dto.get("records", [])
        self.register_supply(supply, records)
        return "<<SupplySaved>>"

    def register_supply(self, supply: Supply, records: list[SupplyRecord]) -> int:
        """Register a supply with multiple records.

        Args:
            supply: Supply model instance.
            records: List of SupplyRecord instances.

        Returns:
            ID of the created supply.

        Raises:
            ValueError: If no records provided.
        """
        if not records:
            raise ValueError("Supply must contain at least one record")

        # Convert Supply to dict
        supply_data = {
            "supply_date": supply.supply_date,
            "supplier_id": supply.supplier_id,
            "warehouse_id": supply.warehouse_id,
            "storekeeper_id": supply.storekeeper_id
        }
        supply_id = self.supply_dao.insert(supply_data)
        supply.id = supply_id

        # Insert records (Observer will update inventory)
        for rec in records:
            rec.supply_id = supply_id
            record_data = {
                "supply_id": supply_id,
                "component_id": rec.component_id,
                "quantity": rec.quantity,
                "price": rec.price
            }
            record_id = self.record_dao.insert(record_data)
            rec.id = record_id

        return supply_id

    def list_all(self) -> list[Supply]:
        """Get all supplies as model instances.

        Returns:
            List of Supply instances.
        """
        dicts = self.supply_dao.find_all()
        supplies = []
        for d in dicts:
            # Convert ISO date string to date object
            date_str = d["supply_date"]
            if isinstance(date_str, str):
                d["supply_date"] = datetime.fromisoformat(date_str).date()
            supplies.append(Supply(**d))
        return supplies
