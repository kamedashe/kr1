"""API endpoints for order management."""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional

from ..core.auth import get_current_active_user
from ..services.order_service import OrderService
from ..dao.order_dao import OrderDAO
from ..db.database import get_connection

router = APIRouter(prefix="/orders", tags=["orders"])


class OrderCreate(BaseModel):
    """Schema for creating an order."""
    supplier: str
    status: str = "pending"


class OrderUpdate(BaseModel):
    """Schema for updating an order."""
    supplier: Optional[str] = None
    status: Optional[str] = None


class OrderResponse(BaseModel):
    """Schema for order response."""
    id: int
    order_id: Optional[int] = None
    supplier: str
    status: str
    date: Optional[str] = None

    class Config:
        from_attributes = True


def get_order_service():
    """Dependency to get order service."""
    conn = get_connection()
    dao = OrderDAO(conn)
    return OrderService(dao)


@router.get("/", response_model=list[dict])
async def list_orders(
    service: OrderService = Depends(get_order_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get all orders."""
    orders = service.list_all()
    return orders


@router.post("/", response_model=dict, status_code=201)
async def create_order(
    order: OrderCreate,
    service: OrderService = Depends(get_order_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Create a new order."""
    try:
        result = service.create(order.model_dump())
        return {"id": result.get("id"), "message": "Order created successfully", "status": "Очікує"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{order_id}")
async def delete_order(
    order_id: int,
    service: OrderService = Depends(get_order_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Delete an order."""
    try:
        # Note: OrderService doesn't have delete, we'll call DAO directly
        service.order_dao.delete(order_id)
        return {"message": "Order deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
