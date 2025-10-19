import sqlite3
import pytest
from dao.warehouse_dao import WarehouseDAO


@pytest.fixture
def dao():
    conn = sqlite3.connect(':memory:')
    return WarehouseDAO(conn)


def test_insert_and_find_by_id(dao):
    """Test inserting and finding warehouse by ID."""
    data = {"name": "Main", "location": "Kyiv"}
    w_id = dao.insert(data)
    assert w_id > 0

    result = dao.find_by_id(w_id)
    assert result is not None
    assert result["name"] == "Main"
    assert result["location"] == "Kyiv"


def test_update_and_find_all(dao):
    """Test updating warehouse and retrieving all."""
    data = {"name": "Main", "location": "Kyiv"}
    w_id = dao.insert(data)

    # Update
    update_data = {"id": w_id, "name": "Updated", "location": "Kyiv"}
    dao.update(update_data)

    all_ws = dao.find_all()
    assert any(x["name"] == "Updated" for x in all_ws)


def test_delete(dao):
    """Test deleting a warehouse."""
    data = {"name": "Delete", "location": "Lviv"}
    w_id = dao.insert(data)

    ok = dao.delete(w_id)
    assert ok
    assert dao.find_by_id(w_id) is None
