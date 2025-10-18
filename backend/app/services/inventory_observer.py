import logging

from ..dao.component_dao import ComponentDAO

logger = logging.getLogger(__name__)


class InventoryObserver:
    """Updates component inventory after supply record insertion.

    Implements Observer pattern to automatically increment stock levels
    when new supply records are added.
    """

    def __init__(self, component_dao: ComponentDAO):
        self.component_dao = component_dao

    def update(self, record_data: dict):
        """Update component inventory based on supply record.

        Args:
            record_data: Dictionary with 'component_id' and 'quantity' keys.
        """
        component_id = record_data["component_id"]
        quantity = record_data["quantity"]

        self.component_dao.update_quantity(component_id, quantity)
        logger.info(f"Inventory updated: +{quantity} for component {component_id}")
