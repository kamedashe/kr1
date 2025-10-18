import sqlite3
import pytest
from datetime import date, datetime
from dao.supply_dao import SupplyDAO
from dao.supplier_dao import SupplierDAO
from dao.warehouse_dao import WarehouseDAO
from dao.storekeeper_dao import StorekeeperDAO


@pytest.fixture
def dao():
    conn = sqlite3.connect(':memory:')
    # Add related tables and records for FK
    SupplierDAO(conn).insert({"name": "S1", "contact_info": "s1"})
    WarehouseDAO(conn).insert({"name": "W1", "location": "Lviv"})
    StorekeeperDAO(conn).insert({"name": "K1", "warehouse_id": 1})
    return SupplyDAO(conn)


def test_insert_and_find_all(dao):
    """Test inserting and finding all supplies."""
    data = {
        "supply_date": date(2025, 5, 30),
        "supplier_id": 1,
        "warehouse_id": 1,
        "storekeeper_id": 1
    }
    s_id = dao.insert(data)
    assert s_id > 0

    all_s = dao.find_all()
    assert any(x["id"] == s_id for x in all_s)

    # Convert date string back to date object for comparison
    first_supply_date = all_s[0]["supply_date"]
    if isinstance(first_supply_date, str):
        first_supply_date = datetime.fromisoformat(first_supply_date).date()
    assert first_supply_date == date(2025, 5, 30)


def test_find_by_id(dao):
    """Test finding supply by ID."""
    data = {
        "supply_date": date(2024, 1, 1),
        "supplier_id": 1,
        "warehouse_id": 1,
        "storekeeper_id": 1
    }
    s_id = dao.insert(data)

    found = dao.find_by_id(s_id)
    assert found is not None

    # Convert date string to date object for comparison
    found_date = found["supply_date"]
    if isinstance(found_date, str):
        found_date = datetime.fromisoformat(found_date).date()

    assert found_date == date(2024, 1, 1)
    assert found["supplier_id"] == 1
    assert found["warehouse_id"] == 1
    assert found["storekeeper_id"] == 1
