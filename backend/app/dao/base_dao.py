"""Base DAO class with common interface for all data access objects."""
import sqlite3
from abc import ABC, abstractmethod
from typing import Optional, Any


class BaseDAO(ABC):
    """Abstract base class for all DAO implementations.

    Provides a consistent interface for CRUD operations across all entities.
    All DAOs should return dictionaries for consistency and serialization.
    """

    def __init__(self, conn: sqlite3.Connection):
        """Initialize DAO with database connection.

        Args:
            conn: SQLite database connection with foreign_keys enabled.
        """
        self.conn = conn
        self._ensure_table()

    @abstractmethod
    def _ensure_table(self):
        """Create table if it doesn't exist. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def insert(self, data: dict) -> int:
        """Insert a new record.

        Args:
            data: Dictionary with entity fields.

        Returns:
            ID of the inserted record.
        """
        pass

    @abstractmethod
    def update(self, data: dict) -> bool:
        """Update an existing record.

        Args:
            data: Dictionary with entity fields including 'id'.

        Returns:
            True if record was updated, False otherwise.
        """
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> bool:
        """Delete a record by ID.

        Args:
            entity_id: ID of the record to delete.

        Returns:
            True if record was deleted, False otherwise.
        """
        pass

    @abstractmethod
    def find_by_id(self, entity_id: int) -> Optional[dict]:
        """Find a record by ID.

        Args:
            entity_id: ID of the record to find.

        Returns:
            Dictionary with entity fields or None if not found.
        """
        pass

    @abstractmethod
    def find_all(self) -> list[dict]:
        """Find all records.

        Returns:
            List of dictionaries with entity fields.
        """
        pass

    def _row_to_dict(self, row: sqlite3.Row, fields: list[str]) -> dict:
        """Convert database row to dictionary.

        Args:
            row: Database row from cursor.fetchone().
            fields: List of field names in order.

        Returns:
            Dictionary mapping field names to values.
        """
        if row is None:
            return None
        return {field: row[i] for i, field in enumerate(fields)}

    def _rows_to_dicts(self, rows: list[sqlite3.Row], fields: list[str]) -> list[dict]:
        """Convert multiple database rows to list of dictionaries.

        Args:
            rows: List of database rows from cursor.fetchall().
            fields: List of field names in order.

        Returns:
            List of dictionaries mapping field names to values.
        """
        return [self._row_to_dict(row, fields) for row in rows]
