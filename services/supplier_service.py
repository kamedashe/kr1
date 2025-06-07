from dao.supplier_dao import SupplierDAO

class SupplierService:
    def __init__(self, dao: SupplierDAO):
        self.dao = dao

    def create(self, dto: dict) -> int:
        return self.dao.insert(dto)

    def list_all(self) -> list[dict]:
        return self.dao.select_all()

    def update(self, pk: int, dto: dict) -> int:
        return self.dao.update(pk, dto)

    def delete(self, pk: int) -> int:
        return self.dao.delete(pk)
