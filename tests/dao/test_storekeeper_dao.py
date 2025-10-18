import sqlite3
import pytest
from dao.storekeeper_dao import StorekeeperDAO
from dao.warehouse_dao import WarehouseDAO


@pytest.fixture
def dao():
    conn = sqlite3.connect(':memory:')
    # Create warehouse table for foreign key
    WarehouseDAO(conn).insert({"name": "W1", "location": "X"})
    return StorekeeperDAO(conn)


def test_insert_and_find_by_id(dao):
    """Test inserting and finding storekeeper by ID."""
    data = {"name": "Ivan", "warehouse_id": 1}
    k_id = dao.insert(data)
    assert k_id > 0

    found = dao.find_by_id(k_id)
    assert found is not None
    assert found["name"] == "Ivan"
    assert found["warehouse_id"] == 1


def test_update_and_find_all(dao):
    """Test updating storekeeper and retrieving all."""
    data = {"name": "Ivan", "warehouse_id": 1}
    k_id = dao.insert(data)

    # Update
    update_data = {"id": k_id, "name": "Stepan", "warehouse_id": 1}
    dao.update(update_data)

    all_k = dao.find_all()
    assert any(x["name"] == "Stepan" for x in all_k)


def test_delete(dao):
    """Test deleting a storekeeper."""
    data = {"name": "Petro", "warehouse_id": 1}
    k_id = dao.insert(data)

    assert dao.delete(k_id)
    assert dao.find_by_id(k_id) is None
