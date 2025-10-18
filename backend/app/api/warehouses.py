"""API endpoints for warehouse management."""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from ..core.auth import get_current_active_user
from ..services.warehouse_service import WarehouseService
from ..dao.warehouse_dao import WarehouseDAO
from ..models.warehouse import Warehouse
from ..db.database import get_connection

router = APIRouter(prefix="/warehouses", tags=["warehouses"])


class WarehouseCreate(BaseModel):
    """Schema for creating a warehouse."""
    name: str
    location: str = ""


class WarehouseUpdate(BaseModel):
    """Schema for updating a warehouse."""
    name: str
    location: str = ""


class WarehouseResponse(BaseModel):
    """Schema for warehouse response."""
    id: int | None
    name: str
    location: str

    class Config:
        from_attributes = True


def get_warehouse_service():
    """Dependency to get warehouse service."""
    conn = get_connection()
    dao = WarehouseDAO(conn)
    return WarehouseService(dao)


@router.get("/", response_model=list[WarehouseResponse])
async def list_warehouses(
    service: WarehouseService = Depends(get_warehouse_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get all warehouses."""
    warehouses = service.list_all()
    return warehouses


@router.get("/stock-levels", response_model=list[dict])
async def get_stock_levels(
    service: WarehouseService = Depends(get_warehouse_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get inventory stock levels across all warehouses."""
    stock_data = service.get_stock_levels()
    return stock_data


@router.get("/{warehouse_id}", response_model=WarehouseResponse)
async def get_warehouse(
    warehouse_id: int,
    service: WarehouseService = Depends(get_warehouse_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get a warehouse by ID."""
    try:
        warehouse = service.get_by_id(warehouse_id)
        return warehouse
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=dict)
async def create_warehouse(
    warehouse: WarehouseCreate,
    service: WarehouseService = Depends(get_warehouse_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Create a new warehouse."""
    try:
        wh = Warehouse(name=warehouse.name, location=warehouse.location)
        warehouse_id = service.create(wh)
        return {"id": warehouse_id, "message": "Warehouse created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{warehouse_id}")
async def update_warehouse(
    warehouse_id: int,
    warehouse: WarehouseUpdate,
    service: WarehouseService = Depends(get_warehouse_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Update a warehouse."""
    try:
        wh = Warehouse(id=warehouse_id, name=warehouse.name, location=warehouse.location)
        success = service.update(wh)
        if success:
            return {"message": "Warehouse updated successfully"}
        raise HTTPException(status_code=400, detail="Update failed")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{warehouse_id}")
async def delete_warehouse(
    warehouse_id: int,
    service: WarehouseService = Depends(get_warehouse_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Delete a warehouse."""
    try:
        success = service.delete(warehouse_id)
        if success:
            return {"message": "Warehouse deleted successfully"}
        raise HTTPException(status_code=400, detail="Delete failed")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
