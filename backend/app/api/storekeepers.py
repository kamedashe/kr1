"""API endpoints for storekeeper management."""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from ..core.auth import get_current_active_user
from ..services.storekeeper_service import StorekeeperService
from ..dao.storekeeper_dao import StorekeeperDAO
from ..models.storekeeper import Storekeeper
from ..db.database import get_connection

router = APIRouter(prefix="/storekeepers", tags=["storekeepers"])


class StorekeeperCreate(BaseModel):
    """Schema for creating a storekeeper."""
    name: str
    warehouse_id: int


class StorekeeperUpdate(BaseModel):
    """Schema for updating a storekeeper."""
    name: str
    warehouse_id: int


class StorekeeperResponse(BaseModel):
    """Schema for storekeeper response."""
    id: int | None
    name: str
    warehouse_id: int

    class Config:
        from_attributes = True


def get_storekeeper_service():
    """Dependency to get storekeeper service."""
    conn = get_connection()
    dao = StorekeeperDAO(conn)
    return StorekeeperService(dao)


@router.get("/", response_model=list[StorekeeperResponse])
async def list_storekeepers(
    service: StorekeeperService = Depends(get_storekeeper_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get all storekeepers."""
    storekeepers = service.list_all()
    return storekeepers


@router.get("/{storekeeper_id}", response_model=StorekeeperResponse)
async def get_storekeeper(
    storekeeper_id: int,
    service: StorekeeperService = Depends(get_storekeeper_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get a storekeeper by ID."""
    try:
        storekeeper = service.get_by_id(storekeeper_id)
        return storekeeper
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=dict)
async def create_storekeeper(
    storekeeper: StorekeeperCreate,
    service: StorekeeperService = Depends(get_storekeeper_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Create a new storekeeper."""
    try:
        sk = Storekeeper(name=storekeeper.name, warehouse_id=storekeeper.warehouse_id)
        storekeeper_id = service.create(sk)
        return {"id": storekeeper_id, "message": "Storekeeper created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{storekeeper_id}")
async def update_storekeeper(
    storekeeper_id: int,
    storekeeper: StorekeeperUpdate,
    service: StorekeeperService = Depends(get_storekeeper_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Update a storekeeper."""
    try:
        sk = Storekeeper(id=storekeeper_id, name=storekeeper.name, warehouse_id=storekeeper.warehouse_id)
        success = service.update(sk)
        if success:
            return {"message": "Storekeeper updated successfully"}
        raise HTTPException(status_code=400, detail="Update failed")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{storekeeper_id}")
async def delete_storekeeper(
    storekeeper_id: int,
    service: StorekeeperService = Depends(get_storekeeper_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Delete a storekeeper."""
    try:
        success = service.delete(storekeeper_id)
        if success:
            return {"message": "Storekeeper deleted successfully"}
        raise HTTPException(status_code=400, detail="Delete failed")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
