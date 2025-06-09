from db.database import get_connection
from ui.main_window import MainWindow
from controllers.supplier_controller import SupplierController
from controllers.component_controller import ComponentController
from controllers.orders_controller import OrderController
from controllers.report_controller import ReportController
from controllers.supply_controller import SupplyController
from services.supplier_service import SupplierService
from services.component_service import ComponentService
from services.warehouse_service import WarehouseService
from services.storekeeper_service import StorekeeperService
from services.supply_service import SupplyService
from services.inventory_observer import InventoryObserver
from services.order_service import OrderService
from services.contract_service import ContractService
from services.report_service import ReportService
from services.history_service import HistoryService
from dao.supplier_dao import SupplierDAO
from dao.component_dao import ComponentDAO
from dao.warehouse_dao import WarehouseDAO
from dao.storekeeper_dao import StorekeeperDAO
from dao.supply_dao import SupplyDAO
from dao.supply_record_dao import SupplyRecordDAO
from dao.order_dao import OrderDAO
from dao.contract_dao import ContractDAO
from dao.history_dao import HistoryDAO


class WarehouseController:
    def __init__(self, view, service: WarehouseService):
        self.view = view
        self.service = service


class StorekeeperController:
    def __init__(self, view, service: StorekeeperService):
        self.view = view
        self.service = service




def main():
    app = MainWindow()
    conn = get_connection()

    nb = app.children.get("!notebook")
    tabs = nb.tabs()
    reports_tab = nb.nametowidget(tabs[0])
    suppliers_tab = nb.nametowidget(tabs[1])
    orders_tab = nb.nametowidget(tabs[2])
    warehouse_tab = nb.nametowidget(tabs[3])
    component_tab = nb.nametowidget(tabs[4])
    storekeeper_tab = nb.nametowidget(tabs[5])
    supply_tab = nb.nametowidget(tabs[6])

    reports_ctrl = ReportController(
        reports_tab,
        ReportService(),
        HistoryService(HistoryDAO()),
    )
    reports_tab.set_controller(reports_ctrl)

    supplier_ctrl = SupplierController(
        SupplierService(SupplierDAO(conn)),
        suppliers_tab,
    )
    suppliers_tab.set_controller(supplier_ctrl)

    orders_ctrl = OrdersController(
        orders_tab,
        OrderService(OrderDAO(conn)),
        ContractService(ContractDAO()),
    )
    orders_tab.set_controller(orders_ctrl)

    warehouse_ctrl = WarehouseController(
        warehouse_tab,
        WarehouseService(WarehouseDAO(conn)),
    )

    component_ctrl = ComponentController(
        ComponentService(ComponentDAO(conn)),
        component_tab,
    )

    storekeeper_ctrl = StorekeeperController(
        storekeeper_tab,
        StorekeeperService(StorekeeperDAO(conn)),
    )

    supply_ctrl = SupplyController(
        supply_tab,
        SupplyService(
            SupplyDAO(conn),
            SupplyRecordDAO(conn, InventoryObserver(ComponentDAO(conn))),
        ),
    )
    supply_tab.set_controller(supply_ctrl)

    app.mainloop()


if __name__ == "__main__":
    main()
