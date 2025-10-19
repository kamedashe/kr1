from ..dao.order_dao import OrderDAO


class OrderService:
    """Facade for order management via DAO."""

    def __init__(self, order_dao: OrderDAO):
        self.order_dao = order_dao

    def create(self, dto: dict) -> dict:
        order_id = self.order_dao.insert(dto)
        dto = dict(dto)
        if order_id is not None:
            dto["id"] = order_id
        return dto

    def list_all(self) -> list[dict]:
        return self.order_dao.select_all()
