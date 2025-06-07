from dao.component_dao import ComponentDAO
from models.component import Component

class ComponentService:
    """Facade over :class:`ComponentDAO` with basic validation."""

    def __init__(self, dao: ComponentDAO):
        self.dao = dao

    def create(self, comp: Component) -> int:
        if not comp.validate():
            raise ValueError("Invalid component data")
        return self.dao.insert(comp)

    def list_all(self) -> list[Component]:
        return self.dao.select_all()

    def get_by_id(self, comp_id: int) -> Component:
        comp = self.dao.find_by_id(comp_id)
        if comp is None:
            raise ValueError("Component not found")
        return comp

    def update(self, comp: Component) -> bool:
        if not comp.validate():
            raise ValueError("Invalid component data")
        return self.dao.update(comp)

    def delete(self, comp_id: int) -> bool:
        return self.dao.delete(comp_id)

    def increment_stock(self, comp_id: int, delta: int) -> None:
        if not isinstance(comp_id, int) or not isinstance(delta, int):
            raise ValueError("IDs and delta must be integers")
        self.dao.update_quantity(comp_id, delta)
