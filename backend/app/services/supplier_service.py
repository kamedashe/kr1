from ..dao.supplier_dao import SupplierDAO
from ..models.supplier import Supplier


class SupplierService:
    """Facade over SupplierDAO with validation and model conversion."""

    def __init__(self, dao: SupplierDAO):
        self.dao = dao

    def create(self, data: dict) -> int:
        """Create a new supplier from dictionary data.

        Args:
            data: Dictionary with 'name' and optional 'contact_info'.

        Returns:
            ID of the created supplier.

        Raises:
            ValueError: If validation fails.
        """
        # Validate using model
        supplier = Supplier(name=data["name"], contact_info=data.get("contact_info", ""))
        if not supplier.validate():
            raise ValueError("Invalid supplier data")

        return self.dao.insert(data)

    def list_all(self) -> list[Supplier]:
        """Get all suppliers as model instances.

        Returns:
            List of Supplier instances.
        """
        dicts = self.dao.find_all()
        return [Supplier(**d) for d in dicts]

    def get_by_id(self, supplier_id: int) -> Supplier:
        """Get supplier by ID.

        Args:
            supplier_id: ID of the supplier.

        Returns:
            Supplier instance.

        Raises:
            ValueError: If supplier not found.
        """
        data = self.dao.find_by_id(supplier_id)
        if data is None:
            raise ValueError("Supplier not found")
        return Supplier(**data)

    def update(self, data: dict) -> bool:
        """Update an existing supplier.

        Args:
            data: Dictionary with 'id', 'name', and optional 'contact_info'.

        Returns:
            True if updated successfully.

        Raises:
            ValueError: If validation fails.
        """
        # Validate using model
        supplier = Supplier(id=data.get("id"), name=data["name"], contact_info=data.get("contact_info", ""))
        if not supplier.validate():
            raise ValueError("Invalid supplier data")

        return self.dao.update(data)

    def delete(self, supplier_id: int) -> bool:
        """Delete a supplier.

        Args:
            supplier_id: ID of the supplier to delete.

        Returns:
            True if deleted successfully.
        """
        return self.dao.delete(supplier_id)
