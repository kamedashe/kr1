from dao.order_dao import OrderDAO


class OrderService:
    """Facade for order management via DAO."""

    def __init__(self, order_dao: OrderDAO):
        self.order_dao = order_dao

    def create(self, dto: dict) -> dict:
        order_id = self.order_dao.insert(dto)
        order = dict(dto)
        order["id"] = order_id
        return order

    def list_all(self) -> list[dict]:
        return self.order_dao.find_all()
