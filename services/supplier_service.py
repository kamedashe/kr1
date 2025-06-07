from dao.supplier_dao import SupplierDAO
from models.supplier import Supplier

class SupplierService:
    def __init__(self, dao: SupplierDAO):
        self.dao = dao

    def create(self, supplier: Supplier) -> int:
        return self.dao.insert(supplier)

    def list_all(self) -> list[Supplier]:
        return self.dao.find_all()

    def update(self, supplier: Supplier) -> bool:
        return self.dao.update(supplier)

    def delete(self, supplier_id: int) -> bool:
        return self.dao.delete(supplier_id)
