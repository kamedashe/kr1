"""API endpoints for component management."""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from ..core.auth import get_current_active_user
from ..services.component_service import ComponentService
from ..dao.component_dao import ComponentDAO
from ..db.database import get_connection

router = APIRouter(prefix="/components", tags=["components"])


class ComponentCreate(BaseModel):
    """Schema for creating a component."""
    name: str
    unit: str
    qty: int = 0


class ComponentUpdate(BaseModel):
    """Schema for updating a component."""
    name: str
    unit: str
    qty: int


class ComponentResponse(BaseModel):
    """Schema for component response."""
    id: int
    name: str
    unit: str
    qty: int

    class Config:
        from_attributes = True


def get_component_service():
    """Dependency to get component service."""
    conn = get_connection()
    dao = ComponentDAO(conn)
    return ComponentService(dao)


@router.get("/", response_model=list[dict])
async def list_components(
    service: ComponentService = Depends(get_component_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get all components."""
    components = service.list_all()
    return components


@router.get("/{component_id}", response_model=dict)
async def get_component(
    component_id: int,
    service: ComponentService = Depends(get_component_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get a component by ID."""
    try:
        component = service.get_by_id(component_id)
        return component
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=dict)
async def create_component(
    component: ComponentCreate,
    service: ComponentService = Depends(get_component_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Create a new component."""
    try:
        component_id = service.create(component.model_dump())
        return {"id": component_id, "message": "Component created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{component_id}")
async def update_component(
    component_id: int,
    component: ComponentUpdate,
    service: ComponentService = Depends(get_component_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Update a component."""
    try:
        data = component.model_dump()
        success = service.update(component_id, data)
        if success:
            return {"message": "Component updated successfully"}
        raise HTTPException(status_code=400, detail="Update failed")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{component_id}")
async def delete_component(
    component_id: int,
    service: ComponentService = Depends(get_component_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Delete a component."""
    try:
        success = service.delete(component_id)
        if success:
            return {"message": "Component deleted successfully"}
        raise HTTPException(status_code=400, detail="Delete failed")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
