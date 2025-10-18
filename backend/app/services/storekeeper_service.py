from ..dao.storekeeper_dao import StorekeeperDAO
from ..models.storekeeper import Storekeeper


class StorekeeperService:
    """Facade over StorekeeperDAO with validation and model conversion."""

    def __init__(self, dao: StorekeeperDAO):
        self.dao = dao

    def create(self, keeper: Storekeeper) -> int:
        """Create a new storekeeper.

        Args:
            keeper: Storekeeper model instance.

        Returns:
            ID of the created storekeeper.

        Raises:
            ValueError: If validation fails.
        """
        keeper.validate()
        data = {"name": keeper.name, "warehouse_id": keeper.warehouse_id}
        return self.dao.insert(data)

    def update(self, keeper: Storekeeper) -> bool:
        """Update an existing storekeeper.

        Args:
            keeper: Storekeeper model instance with ID.

        Returns:
            True if updated successfully.

        Raises:
            ValueError: If validation fails or ID is missing.
        """
        if keeper.id is None:
            raise ValueError("Storekeeper must have ID before update")
        keeper.validate()
        data = {"id": keeper.id, "name": keeper.name, "warehouse_id": keeper.warehouse_id}
        return self.dao.update(data)

    def delete(self, kid: int) -> bool:
        """Delete a storekeeper.

        Args:
            kid: ID of the storekeeper to delete.

        Returns:
            True if deleted successfully.

        Raises:
            ValueError: If ID is not an integer.
        """
        if not isinstance(kid, int):
            raise ValueError("ID must be int")
        return self.dao.delete(kid)

    def get_by_id(self, kid: int) -> Storekeeper:
        """Get storekeeper by ID.

        Args:
            kid: ID of the storekeeper.

        Returns:
            Storekeeper instance.

        Raises:
            ValueError: If ID is invalid or storekeeper not found.
        """
        if not isinstance(kid, int):
            raise ValueError("ID must be int")
        data = self.dao.find_by_id(kid)
        if data is None:
            raise ValueError("Storekeeper not found")
        return Storekeeper(**data)

    def list_all(self) -> list[Storekeeper]:
        """Get all storekeepers as model instances.

        Returns:
            List of Storekeeper instances.
        """
        dicts = self.dao.find_all()
        return [Storekeeper(**d) for d in dicts]