import pytest
from controllers.report_controller import ReportController
from controllers.supplier_controller import SupplierController
from controllers.component_controller import ComponentController
from controllers.supply_controller import SupplyController
from controllers.orders_controller import OrderController, OrdersController

def test_report_controller_methods():
    assert hasattr(ReportController, "generate_report")
    assert hasattr(ReportController, "show_supply_history")


def test_supplier_controller_methods():
    assert hasattr(SupplierController, "on_add")
    assert hasattr(SupplierController, "on_update")
    assert hasattr(SupplierController, "on_delete")


def test_component_controller_methods():
    assert hasattr(ComponentController, "on_add")
    assert hasattr(ComponentController, "on_update")
    assert hasattr(ComponentController, "on_delete")


def test_supply_controller_methods():
    assert hasattr(SupplyController, "register_supply")


def test_order_controller_methods():
    assert hasattr(OrdersController, "create_order")
    assert hasattr(OrdersController, "check_contract")
