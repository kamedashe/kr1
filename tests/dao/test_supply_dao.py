import sqlite3
import pytest
from datetime import date
from models.supply import Supply
from dao.supply_dao import SupplyDAO
from dao.supplier_dao import SupplierDAO
from dao.warehouse_dao import WarehouseDAO
from dao.storekeeper_dao import StorekeeperDAO
from models.supplier import Supplier
from models.warehouse import Warehouse
from models.storekeeper import Storekeeper

@pytest.fixture
def dao():
    conn = sqlite3.connect(':memory:')
    # Додаємо пов’язані таблиці й записи для FK
    SupplierDAO(conn).insert(Supplier(name="S1", contact_info="s1"))
    WarehouseDAO(conn).insert(Warehouse(name="W1", location="Lviv"))
    StorekeeperDAO(conn).insert(Storekeeper(name="K1", warehouse_id=1))
    return SupplyDAO(conn)

def test_insert_and_find_all(dao):
    s = Supply(supply_date=date(2025, 5, 30), supplier_id=1, warehouse_id=1, storekeeper_id=1)
    s_id = dao.insert(s)
    assert s_id > 0
    all_s = dao.find_all()
    assert any(x.id == s_id for x in all_s)
    assert all_s[0].supply_date == date(2025, 5, 30)


def test_find_by_id(dao):
    s = Supply(supply_date=date(2024, 1, 1), supplier_id=1, warehouse_id=1, storekeeper_id=1)
    s_id = dao.insert(s)
    found = dao.find_by_id(s_id)
    assert found is not None
    assert found.supply_date == date(2024, 1, 1)
    assert found.supplier_id == 1
    assert found.warehouse_id == 1
    assert found.storekeeper_id == 1
