import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from db.database import get_connection
from dao.component_dao import ComponentDAO


@pytest.fixture
def dao():
    conn = get_connection(':memory:')
    return ComponentDAO(conn)


@pytest.fixture
def component_dao():
    conn = get_connection(':memory:')
    return ComponentDAO(conn)


@pytest.fixture
def sample_component():
    return {"name": "Bolt", "unit": "pcs", "quantity_in_stock": 10}


def test_insert_and_select(component_dao, sample_component):
    """Test inserting and selecting component."""
    cid = component_dao.insert(sample_component)
    assert cid > 0

    stored = component_dao.find_by_id(cid)
    assert stored is not None
    assert stored["name"] == sample_component["name"]
    assert stored["quantity_in_stock"] == sample_component["quantity_in_stock"]


def test_update_quantity(dao):
    """Test updating component quantity."""
    data = {"name": "Nut", "unit": "pcs", "quantity_in_stock": 5}
    comp_id = dao.insert(data)

    dao.update_quantity(comp_id, 3)

    updated = dao.find_by_id(comp_id)
    assert updated["quantity_in_stock"] == 8
