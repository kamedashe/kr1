import sqlite3
import json

class OrderDAO:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self._ensure_table()

    def _ensure_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT
            )
            """
        )
        self.conn.commit()

    def insert(self, dto: dict) -> int:
        cur = self.conn.execute(
            "INSERT INTO orders (data) VALUES (?)",
            (json.dumps(dto),),
        )
        self.conn.commit()
        return cur.lastrowid

    def select_all(self) -> list[dict]:
        cur = self.conn.execute("SELECT id, data FROM orders ORDER BY id")
        rows = cur.fetchall()
        result = []
        for row in rows:
            data = json.loads(row["data"] if isinstance(row, sqlite3.Row) else row[1])
            data["id"] = row["id"] if isinstance(row, sqlite3.Row) else row[0]
            result.append(data)
        return result
