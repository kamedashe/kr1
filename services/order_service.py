class OrderService:
    """Simple in-memory order management service."""

    def __init__(self):
        self._orders: list[dict] = []
        self._next_id = 1

    def create(self, dto: dict) -> dict:
        """Create a new order from ``dto`` and return stored representation."""
        order = dict(dto)
        order["id"] = self._next_id
        self._next_id += 1
        self._orders.append(order)
        return order

    def list_all(self) -> list[dict]:
        """Return list of all created orders."""
        return list(self._orders)
