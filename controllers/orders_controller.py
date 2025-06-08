from services.order_service import OrderService
from services.contract_service import ContractService
from ui.orders_tab import OrdersTab


class OrdersController:
    def __init__(self, view: OrdersTab, service: OrderService, contract_service: ContractService):
        self.view = view
        self.service = service
        self.contract_service = contract_service
        view.set_controller(self)

    def create_order(self):
        dto = {}
        self.service.create(dto)
        self.view.refresh(self.service.list_all())

    def check_contract(self):
        self.contract_service.verify()
        self.view.refresh(self.service.list_all())
