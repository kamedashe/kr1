import sqlite3
from typing import Optional

from .base_dao import BaseDAO
from ..models.component import Component


class ComponentDAO(BaseDAO):
    """SQLite-based DAO for components.

    Returns all data as dictionaries for consistency.
    Provides additional method for updating stock quantity.
    """

    def _ensure_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS components (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                unit TEXT NOT NULL,
                quantity_in_stock INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        self.conn.commit()

    def insert(self, data: dict) -> int:
        """Insert a new component.

        Args:
            data: Dictionary with 'name', 'unit', and optional 'quantity_in_stock'.

        Returns:
            ID of the inserted component.
        """
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO components (name, unit, quantity_in_stock) VALUES (?, ?, ?)",
                (data["name"], data["unit"], data.get("quantity_in_stock", 0)),
            )
        return cur.lastrowid

    def find_all(self) -> list[dict]:
        """Find all components ordered by ID.

        Returns:
            List of dictionaries with component data.
        """
        cur = self.conn.execute("SELECT id, name, unit, quantity_in_stock FROM components ORDER BY id")
        return self._rows_to_dicts(cur.fetchall(), ["id", "name", "unit", "quantity_in_stock"])

    def find_by_id(self, entity_id: int) -> Optional[dict]:
        """Find component by ID.

        Args:
            entity_id: ID of the component.

        Returns:
            Dictionary with component data or None if not found.
        """
        cur = self.conn.execute(
            "SELECT id, name, unit, quantity_in_stock FROM components WHERE id = ?",
            (entity_id,),
        )
        row = cur.fetchone()
        return self._row_to_dict(row, ["id", "name", "unit", "quantity_in_stock"])

    def update(self, data: dict) -> bool:
        """Update an existing component.

        Args:
            data: Dictionary with 'id', 'name', 'unit', and 'quantity_in_stock'.

        Returns:
            True if component was updated, False otherwise.
        """
        with self.conn:
            cur = self.conn.execute(
                "UPDATE components SET name = ?, unit = ?, quantity_in_stock = ? WHERE id = ?",
                (data["name"], data["unit"], data["quantity_in_stock"], data["id"]),
            )
        return cur.rowcount > 0

    def update_quantity(self, comp_id: int, delta: int) -> None:
        """Update component stock quantity by delta.

        Args:
            comp_id: ID of the component.
            delta: Amount to add (or subtract if negative) from current stock.
        """
        with self.conn:
            self.conn.execute(
                "UPDATE components SET quantity_in_stock = quantity_in_stock + ? WHERE id = ?",
                (delta, comp_id),
            )

    def delete(self, entity_id: int) -> bool:
        """Delete a component by ID.

        Args:
            entity_id: ID of the component to delete.

        Returns:
            True if component was deleted, False otherwise.
        """
        with self.conn:
            cur = self.conn.execute("DELETE FROM components WHERE id = ?", (entity_id,))
        return cur.rowcount > 0
