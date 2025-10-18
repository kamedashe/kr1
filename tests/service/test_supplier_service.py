import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from services.supplier_service import SupplierService


class MockSupplierDAO:
    """Mock DAO for testing."""

    def __init__(self):
        self.data = {}
        self.auto_id = 1

    def insert(self, data: dict) -> int:
        """Insert supplier data and return ID."""
        supplier_id = self.auto_id
        self.data[supplier_id] = {**data, "id": supplier_id}
        self.auto_id += 1
        return supplier_id

    def find_all(self) -> list[dict]:
        """Return all suppliers as dicts."""
        return list(self.data.values())


def test_create_supplier():
    """Test creating a supplier through service."""
    dao = MockSupplierDAO()
    service = SupplierService(dao)

    # Pass dict instead of model
    supplier_data = {"name": "ACME", "contact_info": "acme@example.com"}
    supplier_id = service.create(supplier_data)

    assert supplier_id == 1
    assert len(service.list_all()) == 1
    assert service.list_all()[0].name == "ACME"
