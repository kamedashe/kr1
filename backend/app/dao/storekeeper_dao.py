import sqlite3
from typing import Optional

from .base_dao import BaseDAO
from ..models.storekeeper import Storekeeper


class StorekeeperDAO(BaseDAO):
    """SQLite-based DAO for storekeepers.

    Returns all data as dictionaries for consistency.
    """

    def _ensure_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS storekeepers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                warehouse_id INTEGER,
                FOREIGN KEY (warehouse_id) REFERENCES warehouses(id)
            )
        """)
        self.conn.commit()

    def insert(self, data: dict) -> int:
        """Insert a new storekeeper.

        Args:
            data: Dictionary with 'name' and optional 'warehouse_id'.

        Returns:
            ID of the inserted storekeeper.
        """
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO storekeepers (name, warehouse_id) VALUES (?, ?)",
                (data["name"], data.get("warehouse_id"))
            )
        return cursor.lastrowid

    def update(self, data: dict) -> bool:
        """Update an existing storekeeper.

        Args:
            data: Dictionary with 'id', 'name', and optional 'warehouse_id'.

        Returns:
            True if storekeeper was updated, False otherwise.
        """
        with self.conn:
            cursor = self.conn.execute(
                "UPDATE storekeepers SET name = ?, warehouse_id = ? WHERE id = ?",
                (data["name"], data.get("warehouse_id"), data["id"])
            )
        return cursor.rowcount > 0

    def delete(self, entity_id: int) -> bool:
        """Delete a storekeeper by ID.

        Args:
            entity_id: ID of the storekeeper to delete.

        Returns:
            True if storekeeper was deleted, False otherwise.
        """
        with self.conn:
            cursor = self.conn.execute(
                "DELETE FROM storekeepers WHERE id = ?",
                (entity_id,)
            )
        return cursor.rowcount > 0

    def find_by_id(self, entity_id: int) -> Optional[dict]:
        """Find storekeeper by ID.

        Args:
            entity_id: ID of the storekeeper.

        Returns:
            Dictionary with storekeeper data or None if not found.
        """
        cursor = self.conn.execute(
            "SELECT id, name, warehouse_id FROM storekeepers WHERE id = ?",
            (entity_id,)
        )
        row = cursor.fetchone()
        return self._row_to_dict(row, ["id", "name", "warehouse_id"])

    def find_all(self) -> list[dict]:
        """Find all storekeepers ordered by name.

        Returns:
            List of dictionaries with storekeeper data.
        """
        cursor = self.conn.execute(
            "SELECT id, name, warehouse_id FROM storekeepers ORDER BY name"
        )
        return self._rows_to_dicts(cursor.fetchall(), ["id", "name", "warehouse_id"])