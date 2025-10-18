import sqlite3
from typing import Optional

from .base_dao import BaseDAO
from ..models.supplier import Supplier


class SupplierDAO(BaseDAO):
    """SQLite-based DAO for suppliers.

    Returns all data as dictionaries for consistency.
    """

    def _ensure_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact_info TEXT
            )
            """
        )
        self.conn.commit()

    def insert(self, data: dict) -> int:
        """Insert a new supplier.

        Args:
            data: Dictionary with 'name' and optional 'contact_info'.

        Returns:
            ID of the inserted supplier.
        """
        cur = self.conn.execute(
            "INSERT INTO suppliers (name, contact_info) VALUES (?, ?)",
            (data["name"], data.get("contact_info", "")),
        )
        self.conn.commit()
        return cur.lastrowid

    def update(self, data: dict) -> bool:
        """Update an existing supplier.

        Args:
            data: Dictionary with 'id', 'name', and optional 'contact_info'.

        Returns:
            True if supplier was updated, False otherwise.
        """
        cur = self.conn.execute(
            "UPDATE suppliers SET name = ?, contact_info = ? WHERE id = ?",
            (data["name"], data.get("contact_info", ""), data["id"]),
        )
        self.conn.commit()
        return cur.rowcount > 0



    def find_by_id(self, entity_id: int) -> Optional[dict]:
        """Find supplier by ID.

        Args:
            entity_id: ID of the supplier.

        Returns:
            Dictionary with supplier data or None if not found.
        """
        cur = self.conn.execute(
            "SELECT id, name, contact_info FROM suppliers WHERE id = ?",
            (entity_id,),
        )
        row = cur.fetchone()
        return self._row_to_dict(row, ["id", "name", "contact_info"])

    def find_all(self) -> list[dict]:
        """Find all suppliers ordered by name.

        Returns:
            List of dictionaries with supplier data.
        """
        cur = self.conn.execute(
            "SELECT id, name, contact_info FROM suppliers ORDER BY name"
        )
        return self._rows_to_dicts(cur.fetchall(), ["id", "name", "contact_info"])

    def find_by_name(self, name_part: str) -> list[dict]:
        """Find suppliers by partial name match.

        Args:
            name_part: Partial name to search for.

        Returns:
            List of dictionaries with matching suppliers.
        """
        pattern = f"%{name_part}%"
        cur = self.conn.execute(
            "SELECT id, name, contact_info FROM suppliers WHERE name LIKE ?",
            (pattern,),
        )
        return self._rows_to_dicts(cur.fetchall(), ["id", "name", "contact_info"])

    def delete(self, entity_id: int) -> bool:
        """Delete a supplier by ID.

        Args:
            entity_id: ID of the supplier to delete.

        Returns:
            True if supplier was deleted, False otherwise.
        """
        cur = self.conn.execute("DELETE FROM suppliers WHERE id = ?", (entity_id,))
        self.conn.commit()
        return cur.rowcount > 0
