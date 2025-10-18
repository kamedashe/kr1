"""
Конфігурація pytest для тестів API
"""
import pytest
import sys
import os

# Додаємо шлях до backend/app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from app.db.database import get_connection


@pytest.fixture(scope="function")
def test_db():
    """Створює тестову БД в пам'яті"""
    conn = get_connection(":memory:")

    # Створюємо таблиці
    conn.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            contact_info TEXT,
            email TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS components (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            price REAL NOT NULL CHECK(price > 0),
            quantity INTEGER NOT NULL CHECK(quantity >= 0)
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS warehouses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            location TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS storekeepers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            warehouse_id INTEGER,
            FOREIGN KEY (warehouse_id) REFERENCES warehouses(id)
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            supplier_id INTEGER NOT NULL,
            component_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity > 0),
            order_date TEXT NOT NULL,
            status TEXT DEFAULT 'Очікує',
            FOREIGN KEY (supplier_id) REFERENCES suppliers(id),
            FOREIGN KEY (component_id) REFERENCES components(id)
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS supplies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            supplier_id INTEGER NOT NULL,
            supply_date TEXT NOT NULL,
            FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
        )
    """)

    conn.commit()

    yield conn

    # Очищення
    conn.close()
