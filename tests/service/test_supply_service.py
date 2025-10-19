import pytest
from unittest.mock import MagicMock
from services.supply_service import SupplyService
from models.supply import Supply
from models.supply_record import SupplyRecord
from datetime import date


@pytest.fixture
def supply_dao():
    return MagicMock()


@pytest.fixture
def record_dao():
    return MagicMock()


@pytest.fixture
def service(supply_dao, record_dao):
    return SupplyService(supply_dao, record_dao)


def test_register_supply_ok(service, supply_dao, record_dao):
    """Test successful supply registration."""
    supply = Supply(
        supply_date=date(2024, 5, 30),
        supplier_id=1,
        warehouse_id=1,
        storekeeper_id=1
    )
    records = [
        SupplyRecord(supply_id=None, component_id=1, quantity=10, price=100.0),
        SupplyRecord(supply_id=None, component_id=2, quantity=5, price=50.0)
    ]

    # Mock DAO to return ID
    supply_dao.insert.return_value = 1
    record_dao.insert.side_effect = [1, 2]  # Return IDs for records

    result = service.register({"supply": supply, "records": records})

    # Verify DAO was called with dict (not model object)
    assert supply_dao.insert.called
    call_args = supply_dao.insert.call_args[0][0]
    assert isinstance(call_args, dict)
    assert call_args["supplier_id"] == 1

    # Verify all records got supply_id set
    assert all(r.supply_id == 1 for r in records)
    assert record_dao.insert.call_count == 2
    assert result == "<<SupplySaved>>"


def test_register_supply_empty_records(service):
    """Test that empty records raises ValueError."""
    supply = Supply(
        supply_date=date(2024, 5, 30),
        supplier_id=1,
        warehouse_id=1,
        storekeeper_id=1
    )
    with pytest.raises(ValueError):
        service.register({"supply": supply, "records": []})
