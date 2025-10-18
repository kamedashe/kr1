"""API endpoints for supply management."""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional

from ..core.auth import get_current_active_user
from ..services.supply_service import SupplyService
from ..dao.supply_dao import SupplyDAO
from ..dao.supply_record_dao import SupplyRecordDAO
from ..services.inventory_observer import InventoryObserver
from ..dao.component_dao import ComponentDAO
from ..db.database import get_connection

router = APIRouter(prefix="/supplies", tags=["supplies"])


class SupplyCreate(BaseModel):
    """Schema for creating a supply."""
    supplier_id: int
    date: Optional[str] = None


class SupplyResponse(BaseModel):
    """Schema for supply response."""
    id: int
    supplier_id: int
    date: Optional[str] = None

    class Config:
        from_attributes = True


def get_supply_service():
    """Dependency to get supply service."""
    conn = get_connection()
    supply_dao = SupplyDAO(conn)
    component_dao = ComponentDAO(conn)
    inventory_observer = InventoryObserver(component_dao)
    supply_record_dao = SupplyRecordDAO(conn, inventory_observer)
    return SupplyService(supply_dao, supply_record_dao)


@router.get("/", response_model=list[dict])
async def list_supplies(
    service: SupplyService = Depends(get_supply_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get all supplies."""
    supplies = service.list_all()
    return supplies


@router.post("/", response_model=dict)
async def create_supply(
    supply: SupplyCreate,
    service: SupplyService = Depends(get_supply_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Create a new supply."""
    try:
        supply_id = service.create(supply.model_dump())
        return {"id": supply_id, "message": "Supply created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{supply_id}")
async def delete_supply(
    supply_id: int,
    service: SupplyService = Depends(get_supply_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Delete a supply."""
    try:
        success = service.delete(supply_id)
        if success:
            return {"message": "Supply deleted successfully"}
        raise HTTPException(status_code=400, detail="Delete failed")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
