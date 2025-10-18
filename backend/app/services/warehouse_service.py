from ..dao.warehouse_dao import WarehouseDAO
from ..models.warehouse import Warehouse


class WarehouseService:
    """Facade over WarehouseDAO with validation and model conversion."""

    def __init__(self, dao: WarehouseDAO):
        self.dao = dao

    def create(self, warehouse: Warehouse) -> int:
        """Create a new warehouse.

        Args:
            warehouse: Warehouse model instance.

        Returns:
            ID of the created warehouse.

        Raises:
            ValueError: If validation fails.
        """
        warehouse.validate()
        data = {"name": warehouse.name, "location": warehouse.location}
        return self.dao.insert(data)

    def update(self, warehouse: Warehouse) -> bool:
        """Update an existing warehouse.

        Args:
            warehouse: Warehouse model instance with ID.

        Returns:
            True if updated successfully.

        Raises:
            ValueError: If validation fails or ID is missing.
        """
        if warehouse.id is None:
            raise ValueError("Warehouse must have ID before update")
        warehouse.validate()
        data = {"id": warehouse.id, "name": warehouse.name, "location": warehouse.location}
        return self.dao.update(data)

    def delete(self, wh_id: int) -> bool:
        """Delete a warehouse.

        Args:
            wh_id: ID of the warehouse to delete.

        Returns:
            True if deleted successfully.

        Raises:
            ValueError: If ID is not an integer.
        """
        if not isinstance(wh_id, int):
            raise ValueError("ID must be int")
        return self.dao.delete(wh_id)

    def get_by_id(self, wh_id: int) -> Warehouse:
        """Get warehouse by ID.

        Args:
            wh_id: ID of the warehouse.

        Returns:
            Warehouse instance.

        Raises:
            ValueError: If ID is invalid or warehouse not found.
        """
        if not isinstance(wh_id, int):
            raise ValueError("ID must be int")
        data = self.dao.find_by_id(wh_id)
        if data is None:
            raise ValueError("Warehouse not found")
        return Warehouse(**data)

    def list_all(self) -> list[Warehouse]:
        """Get all warehouses as model instances.

        Returns:
            List of Warehouse instances.
        """
        dicts = self.dao.find_all()
        return [Warehouse(**d) for d in dicts]

    def get_stock_levels(self) -> list[dict]:
        """Get inventory stock levels across all warehouses.

        Returns:
            List of dictionaries with component, quantity, and unit information.
        """
        # TODO: Implement actual stock level aggregation from warehouse inventory
        # This should query components stored in warehouses
        # For now, return empty list as placeholder
        return []