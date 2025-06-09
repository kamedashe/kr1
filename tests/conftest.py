import pytest

@pytest.fixture
def component_dao(tmp_path):
    from dao.component_dao import ComponentDAO
    from db.database import get_connection
    return ComponentDAO(get_connection(tmp_path/"test.db"))

@pytest.fixture
def sample_component():
    return {"name": "Bolt", "unit": "pcs", "quantity_in_stock": 100}
