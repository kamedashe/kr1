"""Dependencies for FastAPI routes."""
from typing import Generator
import sqlite3


def get_db() -> Generator:
    """Get database connection."""
    try:
        conn = sqlite3.connect("../../db/supply.db")
        conn.row_factory = sqlite3.Row
        yield conn
    finally:
        conn.close()
