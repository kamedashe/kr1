import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from db.database import get_connection
from dao.component_dao import ComponentDAO
from models.component import Component

@pytest.fixture
def dao():
    conn = get_connection(':memory:')   # in‑memory DB
    return ComponentDAO(conn)

@pytest.fixture
def component_dao():
    conn = get_connection(':memory:')
    return ComponentDAO(conn)

@pytest.fixture
def sample_component():
    return {"name": "Bolt", "unit": "pcs", "quantity_in_stock": 10}

def test_insert_and_select(component_dao, sample_component):
    cid = component_dao.insert_component(Component(**sample_component))
    stored = component_dao.select_by_id(cid)
    assert stored.name == sample_component["name"]

def test_update_quantity(dao):
    comp = Component(name='Nut', unit='pcs', quantity_in_stock=5)
    comp_id = dao.insert_component(comp)
    dao.update_quantity(comp_id, 3)
    updated = dao.find_by_id(comp_id)
    assert updated.quantity_in_stock == 8
