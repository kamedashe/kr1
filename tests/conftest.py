import pytest
import sys
import os

# Add the backend directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from app.dao.component_dao import ComponentDAO
from db.database import get_connection





@pytest.fixture
def component_dao(tmp_path):
    return ComponentDAO(get_connection(tmp_path / "t.db"))


@pytest.fixture
def sample_component():
    return {"name": "Bolt", "unit": "pcs", "quantity_in_stock": 100}
