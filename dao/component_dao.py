import sqlite3
from models.component import Component

class ComponentDAO:
    """SQLite-based DAO for components."""

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self._ensure_table()

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

    # CRUD --------------------------------------------------
    def insert(self, comp: Component) -> int:
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO components (name, unit, quantity_in_stock) VALUES (?, ?, ?)",
                (comp.name, comp.unit, comp.quantity_in_stock),
            )
            comp.id = cur.lastrowid
        return comp.id

    def select_all(self) -> list[Component]:
        cur = self.conn.execute("SELECT id, name, unit, quantity_in_stock FROM components ORDER BY id")
        rows = cur.fetchall()
        return [
            Component(id=row[0], name=row[1], unit=row[2], quantity_in_stock=row[3])
            for row in rows
        ]

    def find_by_id(self, comp_id: int) -> Component | None:
        cur = self.conn.execute(
            "SELECT id, name, unit, quantity_in_stock FROM components WHERE id = ?",
            (comp_id,),
        )
        row = cur.fetchone()
        if not row:
            return None
        return Component(id=row[0], name=row[1], unit=row[2], quantity_in_stock=row[3])

    def update(self, comp: Component) -> bool:
        with self.conn:
            cur = self.conn.execute(
                "UPDATE components SET name = ?, unit = ?, quantity_in_stock = ? WHERE id = ?",
                (comp.name, comp.unit, comp.quantity_in_stock, comp.id),
            )
        return cur.rowcount > 0

    def update_quantity(self, comp_id: int, delta: int) -> None:
        with self.conn:
            self.conn.execute(
                "UPDATE components SET quantity_in_stock = quantity_in_stock + ? WHERE id = ?",
                (delta, comp_id),
            )

    def delete(self, comp_id: int) -> bool:
        with self.conn:
            cur = self.conn.execute("DELETE FROM components WHERE id = ?", (comp_id,))
        return cur.rowcount > 0
