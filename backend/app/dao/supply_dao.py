import sqlite3
from typing import Optional
from datetime import datetime

from .base_dao import BaseDAO
from ..models.supply import Supply


class SupplyDAO(BaseDAO):
    """SQLite-based DAO for supplies.

    Returns all data as dictionaries for consistency.
    Handles date serialization to/from ISO format.
    """

    def _ensure_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS supplies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                supplier_id INTEGER,
                warehouse_id INTEGER,
                storekeeper_id INTEGER,
                FOREIGN KEY (supplier_id) REFERENCES suppliers(id),
                FOREIGN KEY (warehouse_id) REFERENCES warehouses(id),
                FOREIGN KEY (storekeeper_id) REFERENCES storekeepers(id)
            )
        """)
        self.conn.commit()

    def insert(self, data: dict) -> int:
        """Insert a new supply.

        Args:
            data: Dictionary with 'supply_date' (date or str), 'supplier_id',
                  'warehouse_id', and 'storekeeper_id'.

        Returns:
            ID of the inserted supply.
        """
        # Convert date to ISO string if needed
        date_str = data["supply_date"]
        if hasattr(date_str, "isoformat"):
            date_str = date_str.isoformat()

        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO supplies (date, supplier_id, warehouse_id, storekeeper_id)
            VALUES (?, ?, ?, ?)
        """, (date_str, data["supplier_id"], data["warehouse_id"], data["storekeeper_id"]))
        self.conn.commit()
        return cursor.lastrowid

    def update(self, data: dict) -> bool:
        """Update an existing supply.

        Args:
            data: Dictionary with 'id', 'supply_date', 'supplier_id',
                  'warehouse_id', and 'storekeeper_id'.

        Returns:
            True if supply was updated, False otherwise.
        """
        # Convert date to ISO string if needed
        date_str = data["supply_date"]
        if hasattr(date_str, "isoformat"):
            date_str = date_str.isoformat()

        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE supplies SET date = ?, supplier_id = ?, warehouse_id = ?, storekeeper_id = ?
            WHERE id = ?
        """, (date_str, data["supplier_id"], data["warehouse_id"], data["storekeeper_id"], data["id"]))
        self.conn.commit()
        return cursor.rowcount > 0

    def delete(self, entity_id: int) -> bool:
        """Delete a supply by ID.

        Args:
            entity_id: ID of the supply to delete.

        Returns:
            True if supply was deleted, False otherwise.
        """
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM supplies WHERE id = ?", (entity_id,))
        self.conn.commit()
        return cursor.rowcount > 0

    def find_all(self) -> list[dict]:
        """Find all supplies.

        Returns:
            List of dictionaries with supply data (dates as ISO strings).
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, date, supplier_id, warehouse_id, storekeeper_id FROM supplies ORDER BY date DESC")
        rows = cursor.fetchall()
        return self._rows_to_dicts(rows, ["id", "supply_date", "supplier_id", "warehouse_id", "storekeeper_id"])

    def find_by_id(self, entity_id: int) -> Optional[dict]:
        """Find supply by ID.

        Args:
            entity_id: ID of the supply.

        Returns:
            Dictionary with supply data or None if not found.
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, date, supplier_id, warehouse_id, storekeeper_id FROM supplies WHERE id = ?", (entity_id,))
        row = cursor.fetchone()
        return self._row_to_dict(row, ["id", "supply_date", "supplier_id", "warehouse_id", "storekeeper_id"])
