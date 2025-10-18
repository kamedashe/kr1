import sqlite3
import pytest
from datetime import date
from dao.supply_record_dao import SupplyRecordDAO
from dao.supply_dao import SupplyDAO
from dao.component_dao import ComponentDAO
from dao.supplier_dao import SupplierDAO
from dao.warehouse_dao import WarehouseDAO
from dao.storekeeper_dao import StorekeeperDAO


@pytest.fixture
def dao():
    conn = sqlite3.connect(':memory:')
    # Create all required tables and records for FK
    SupplierDAO(conn).insert({"name": "S1", "contact_info": "s1"})
    WarehouseDAO(conn).insert({"name": "W1", "location": "Lviv"})
    StorekeeperDAO(conn).insert({"name": "K1", "warehouse_id": 1})
    ComponentDAO(conn).insert({"name": "Comp1", "unit": "pcs", "quantity_in_stock": 100})
    SupplyDAO(conn).insert({
        "supply_date": date(2025, 5, 30),
        "supplier_id": 1,
        "warehouse_id": 1,
        "storekeeper_id": 1
    })
    return SupplyRecordDAO(conn)


def test_insert_and_find_by_supply(dao):
    """Test inserting and finding supply records by supply ID."""
    data = {"supply_id": 1, "component_id": 1, "quantity": 42, "price": 3.14}
    rec_id = dao.insert(data)
    assert rec_id > 0

    found = dao.find_by_supply(1)
    assert any(r["id"] == rec_id and r["quantity"] == 42 for r in found)


def test_delete(dao):
    """Test deleting a supply record."""
    data = {"supply_id": 1, "component_id": 1, "quantity": 1, "price": 1.0}
    rec_id = dao.insert(data)

    assert dao.delete(rec_id)
