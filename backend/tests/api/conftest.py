"""
Конфігурація pytest для тестів API
"""
import pytest
import sys
import os
import tempfile

# Додаємо шлях до backend/app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from app.db.database import get_connection
from app.db import database


# Глобальна тестова БД
TEST_DB_PATH = None


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    """Створює тестову БД один раз для всієї сесії"""
    global TEST_DB_PATH

    # Створюємо тимчасовий файл для тестової БД
    temp_db = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
    TEST_DB_PATH = temp_db.name
    temp_db.close()

    # Підміняємо шлях до БД в модулі database
    original_db_path = database.DEFAULT_DB_PATH
    database.DEFAULT_DB_PATH = TEST_DB_PATH

    # Створюємо структуру БД
    conn = get_connection(TEST_DB_PATH)

    # Створюємо таблиці згідно зі схемою проекту
    conn.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact_info TEXT DEFAULT '',
            email TEXT DEFAULT ''
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS components (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            unit TEXT NOT NULL,
            quantity_in_stock INTEGER DEFAULT 0
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS warehouses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT DEFAULT ''
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
            order_id INTEGER,
            supplier TEXT NOT NULL,
            date TEXT,
            status TEXT DEFAULT 'pending'
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
    conn.close()

    yield TEST_DB_PATH

    # Очищення після всіх тестів
    database.DEFAULT_DB_PATH = original_db_path
    try:
        os.unlink(TEST_DB_PATH)
    except:
        pass


@pytest.fixture(scope="function", autouse=True)
def clear_test_data():
    """Очищає дані з тестової БД перед кожним тестом"""
    if TEST_DB_PATH is None:
        return

    conn = get_connection(TEST_DB_PATH)

    # Очищаємо таблиці
    try:
        conn.execute("DELETE FROM orders")
        conn.execute("DELETE FROM supplies")
        conn.execute("DELETE FROM storekeepers")
        conn.execute("DELETE FROM components")
        conn.execute("DELETE FROM warehouses")
        conn.execute("DELETE FROM suppliers")
        conn.commit()
    except Exception as e:
        print(f"Warning: Failed to clear test data: {e}")
    finally:
        conn.close()

    yield
