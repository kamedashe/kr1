import sqlite3


class OrderDAO:
    """Simple SQLite-based DAO for orders."""

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self._ensure_table()

    def _ensure_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id TEXT,
                supplier TEXT,
                status TEXT,
                date TEXT
            )
            """
        )
        self.conn.commit()

    def insert(self, dto: dict) -> int:
        cur = self.conn.execute(
            "INSERT INTO orders (order_id, supplier, status, date) VALUES (?, ?, ?, ?)",
            (
                dto.get("order_id"),
                dto.get("supplier"),
                dto.get("status"),
                dto.get("date"),
            ),
        )
        self.conn.commit()
        return cur.lastrowid

    def find_all(self) -> list[dict]:
        cur = self.conn.execute(
            "SELECT id, order_id, supplier, status, date FROM orders"
        )
        return [
            {
                "id": row[0],
                "order_id": row[1],
                "supplier": row[2],
                "status": row[3],
                "date": row[4],
            }
            for row in cur.fetchall()
        ]
