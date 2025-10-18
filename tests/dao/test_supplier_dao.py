import sqlite3
import pytest
from dao.supplier_dao import SupplierDAO


@pytest.fixture
def dao():
    conn = sqlite3.connect(':memory:')
    return SupplierDAO(conn)


def test_insert_and_find_by_id(dao):
    """Test inserting and finding supplier by ID."""
    data = {"name": "Sigma", "contact_info": "sig@mail.com"}
    s_id = dao.insert(data)
    assert s_id > 0

    found = dao.find_by_id(s_id)
    assert found is not None
    assert found["name"] == "Sigma"
    assert found["contact_info"] == "sig@mail.com"


def test_update_and_find_all(dao):
    """Test updating supplier and retrieving all."""
    data = {"name": "Beta", "contact_info": "b@b.com"}
    s_id = dao.insert(data)

    # Update
    update_data = {"id": s_id, "name": "Alpha", "contact_info": "b@b.com"}
    dao.update(update_data)

    all_s = dao.find_all()
    assert any(x["name"] == "Alpha" for x in all_s)


def test_delete(dao):
    """Test deleting a supplier."""
    data = {"name": "ToDelete", "contact_info": "none"}
    s_id = dao.insert(data)

    assert dao.delete(s_id)
    assert dao.find_by_id(s_id) is None


def test_find_by_name(dao):
    """Test finding suppliers by partial name."""
    dao.insert({"name": "AlphaComp", "contact_info": "a@a.com"})
    dao.insert({"name": "Betta", "contact_info": "b@b.com"})

    results = dao.find_by_name("Alpha")
    assert len(results) == 1
    assert results[0]["name"] == "AlphaComp"
