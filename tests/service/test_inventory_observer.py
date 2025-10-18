from unittest.mock import MagicMock
from services.inventory_observer import InventoryObserver


def test_update_calls_update_quantity():
    """Test that observer calls update_quantity with correct params."""
    dao = MagicMock()
    obs = InventoryObserver(dao)

    # Pass dict instead of model object
    record_data = {"supply_id": 1, "component_id": 2, "quantity": 5, "price": 99.99}
    obs.update(record_data)

    dao.update_quantity.assert_called_once_with(2, 5)
