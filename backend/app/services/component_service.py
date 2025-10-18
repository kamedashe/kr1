from ..dao.component_dao import ComponentDAO
from ..models.component import Component


class ComponentService:
    """Facade over ComponentDAO with validation and model conversion."""

    def __init__(self, dao: ComponentDAO):
        self.dao = dao

    def create(self, data: dict) -> int:
        """Create a new component.

        Args:
            data: Dictionary with 'name', 'unit', and 'qty' (or 'quantity_in_stock').

        Returns:
            ID of the created component.

        Raises:
            ValueError: If component data is invalid.
        """
        # Normalize field names - accept both 'qty' and 'quantity_in_stock'
        quantity = data.get("qty", data.get("quantity_in_stock", 0))

        comp = Component(
            name=data.get("name", ""),
            unit=data.get("unit", ""),
            quantity_in_stock=quantity
        )

        if not comp.validate():
            raise ValueError("Invalid component data")

        dao_data = {"name": comp.name, "unit": comp.unit, "quantity_in_stock": comp.quantity_in_stock}
        return self.dao.insert(dao_data)

    def list_all(self) -> list[dict]:
        """Get all components as dictionaries.

        Returns:
            List of dictionaries with component data.
        """
        return self.dao.find_all()

    def get_by_id(self, comp_id: int) -> Component:
        """Get component by ID.

        Args:
            comp_id: ID of the component.

        Returns:
            Component instance.

        Raises:
            ValueError: If component not found.
        """
        data = self.dao.find_by_id(comp_id)
        if data is None:
            raise ValueError("Component not found")
        return Component(**data)

    def update(self, comp_id: int, data: dict) -> bool:
        """Update an existing component.

        Args:
            comp_id: ID of the component to update.
            data: Dictionary with 'name', 'unit', and 'qty' (or 'quantity_in_stock').

        Returns:
            True if updated successfully.

        Raises:
            ValueError: If component data is invalid.
        """
        # Normalize field names - accept both 'qty' and 'quantity_in_stock'
        quantity = data.get("qty", data.get("quantity_in_stock", 0))

        comp = Component(
            id=comp_id,
            name=data.get("name", ""),
            unit=data.get("unit", ""),
            quantity_in_stock=quantity
        )

        if not comp.validate():
            raise ValueError("Invalid component data")

        dao_data = {"id": comp.id, "name": comp.name, "unit": comp.unit, "quantity_in_stock": comp.quantity_in_stock}
        return self.dao.update(dao_data)

    def delete(self, comp_id: int) -> bool:
        """Delete a component.

        Args:
            comp_id: ID of the component to delete.

        Returns:
            True if deleted successfully.
        """
        return self.dao.delete(comp_id)

    def increment_stock(self, component_id: int, delta: int) -> None:
        """Increase stock quantity for a component.

        Args:
            component_id: ID of the component.
            delta: Amount to add to stock (can be negative).

        Raises:
            ValueError: If parameters are invalid.
        """
        if not isinstance(component_id, int) or not isinstance(delta, int):
            raise ValueError("component_id and delta must be integers")
        self.dao.update_quantity(component_id, delta)
