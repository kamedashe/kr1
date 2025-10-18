import sqlite3
from typing import Optional

from .base_dao import BaseDAO
from ..models.warehouse import Warehouse


class WarehouseDAO(BaseDAO):
    """SQLite-based DAO for warehouses.

    Returns all data as dictionaries for consistency.
    """

    def _ensure_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS warehouses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT
            )
        """)
        self.conn.commit()

    def insert(self, data: dict) -> int:
        """Insert a new warehouse.

        Args:
            data: Dictionary with 'name' and optional 'location'.

        Returns:
            ID of the inserted warehouse.
        """
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO warehouses (name, location) VALUES (?, ?)",
                (data["name"], data.get("location", ""))
            )
        return cursor.lastrowid

    def update(self, data: dict) -> bool:
        """Update an existing warehouse.

        Args:
            data: Dictionary with 'id', 'name', and optional 'location'.

        Returns:
            True if warehouse was updated, False otherwise.
        """
        with self.conn:
            cursor = self.conn.execute(
                "UPDATE warehouses SET name = ?, location = ? WHERE id = ?",
                (data["name"], data.get("location", ""), data["id"])
            )
        return cursor.rowcount > 0

    def delete(self, entity_id: int) -> bool:
        """Delete a warehouse by ID.

        Args:
            entity_id: ID of the warehouse to delete.

        Returns:
            True if warehouse was deleted, False otherwise.
        """
        with self.conn:
            cursor = self.conn.execute(
                "DELETE FROM warehouses WHERE id = ?",
                (entity_id,)
            )
        return cursor.rowcount > 0

    def find_by_id(self, entity_id: int) -> Optional[dict]:
        """Find warehouse by ID.

        Args:
            entity_id: ID of the warehouse.

        Returns:
            Dictionary with warehouse data or None if not found.
        """
        cursor = self.conn.execute(
            "SELECT id, name, location FROM warehouses WHERE id = ?",
            (entity_id,)
        )
        row = cursor.fetchone()
        return self._row_to_dict(row, ["id", "name", "location"])

    def find_all(self) -> list[dict]:
        """Find all warehouses ordered by name.

        Returns:
            List of dictionaries with warehouse data.
        """
        cursor = self.conn.execute(
            "SELECT id, name, location FROM warehouses ORDER BY name"
        )
        return self._rows_to_dicts(cursor.fetchall(), ["id", "name", "location"])