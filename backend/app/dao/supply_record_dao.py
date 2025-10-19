import sqlite3
import logging
from typing import Optional

from .base_dao import BaseDAO
from ..models.supply_record import SupplyRecord

logger = logging.getLogger(__name__)


class SupplyRecordDAO(BaseDAO):
    """SQLite-based DAO for supply records.

    Returns all data as dictionaries for consistency.
    Supports Observer pattern for inventory updates.

    Args:
        conn: SQLite database connection.
        observer: Optional object with update(record_data: dict) method.
                  Called after successful insert.
    """

    def __init__(self, conn: sqlite3.Connection, observer: Optional[object] = None):
        self.observer = observer
        super().__init__(conn)

    def _ensure_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS supply_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                supply_id INTEGER,
                component_id INTEGER,
                quantity INTEGER,
                price REAL,
                FOREIGN KEY (supply_id) REFERENCES supplies(id),
                FOREIGN KEY (component_id) REFERENCES components(id)
            )
            """
        )
        self.conn.commit()

    def insert(self, data: dict) -> int:
        """Insert a new supply record.

        Args:
            data: Dictionary with 'supply_id', 'component_id', 'quantity', 'price'.

        Returns:
            ID of the inserted record.
        """
        with self.conn:
            cur = self.conn.execute(
                """INSERT INTO supply_records
                       (supply_id, component_id, quantity, price)
                       VALUES (?,?,?,?)""",
                (data["supply_id"], data["component_id"], data["quantity"], data["price"]),
            )
            record_id = cur.lastrowid

        # Notify observer with complete record data
        if self.observer and hasattr(self.observer, "update"):
            try:
                record_data = {**data, "id": record_id}
                self.observer.update(record_data)
            except Exception as e:
                logger.error(f"Observer update failed: {e}")

        return record_id

    def update(self, data: dict) -> bool:
        """Update an existing supply record.

        Args:
            data: Dictionary with 'id', 'supply_id', 'component_id', 'quantity', 'price'.

        Returns:
            True if record was updated, False otherwise.
        """
        with self.conn:
            cur = self.conn.execute(
                """UPDATE supply_records
                   SET supply_id = ?, component_id = ?, quantity = ?, price = ?
                   WHERE id = ?""",
                (data["supply_id"], data["component_id"], data["quantity"], data["price"], data["id"]),
            )
        return cur.rowcount > 0

    def delete(self, entity_id: int) -> bool:
        """Delete a supply record by ID.

        Args:
            entity_id: ID of the record to delete.

        Returns:
            True if record was deleted, False otherwise.
        """
        with self.conn:
            cur = self.conn.execute("DELETE FROM supply_records WHERE id = ?", (entity_id,))
        return cur.rowcount > 0

    def find_by_id(self, entity_id: int) -> Optional[dict]:
        """Find supply record by ID.

        Args:
            entity_id: ID of the record.

        Returns:
            Dictionary with record data or None if not found.
        """
        cur = self.conn.execute(
            """SELECT id, supply_id, component_id, quantity, price
               FROM supply_records WHERE id = ?""",
            (entity_id,),
        )
        row = cur.fetchone()
        return self._row_to_dict(row, ["id", "supply_id", "component_id", "quantity", "price"])

    def find_all(self) -> list[dict]:
        """Find all supply records.

        Returns:
            List of dictionaries with record data.
        """
        cur = self.conn.execute(
            """SELECT id, supply_id, component_id, quantity, price
               FROM supply_records ORDER BY id"""
        )
        return self._rows_to_dicts(cur.fetchall(), ["id", "supply_id", "component_id", "quantity", "price"])

    def find_by_supply(self, supply_id: int) -> list[dict]:
        """Find all records for a specific supply.

        Args:
            supply_id: ID of the supply.

        Returns:
            List of dictionaries with record data.
        """
        cur = self.conn.execute(
            """SELECT id, supply_id, component_id, quantity, price
                   FROM supply_records
                   WHERE supply_id = ?""",
            (supply_id,),
        )
        return self._rows_to_dicts(cur.fetchall(), ["id", "supply_id", "component_id", "quantity", "price"])
