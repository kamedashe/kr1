"""API endpoints for supplier management."""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from ..core.auth import get_current_active_user
from ..services.supplier_service import SupplierService
from ..dao.supplier_dao import SupplierDAO
from ..db.database import get_connection

router = APIRouter(prefix="/suppliers", tags=["suppliers"])


class SupplierCreate(BaseModel):
    """Schema for creating a supplier."""
    name: str
    contact_info: str = ""


class SupplierUpdate(BaseModel):
    """Schema for updating a supplier."""
    name: str
    contact_info: str = ""


class SupplierResponse(BaseModel):
    """Schema for supplier response."""
    id: int
    name: str
    contact_info: str

    class Config:
        from_attributes = True


def get_supplier_service():
    """Dependency to get supplier service."""
    conn = get_connection()
    dao = SupplierDAO(conn)
    return SupplierService(dao)


@router.get("/", response_model=list[SupplierResponse])
async def list_suppliers(
    service: SupplierService = Depends(get_supplier_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get all suppliers."""
    suppliers = service.list_all()
    return suppliers


@router.get("/{supplier_id}", response_model=SupplierResponse)
async def get_supplier(
    supplier_id: int,
    service: SupplierService = Depends(get_supplier_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get a supplier by ID."""
    try:
        supplier = service.get_by_id(supplier_id)
        return supplier
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=dict, status_code=201)
async def create_supplier(
    supplier: SupplierCreate,
    service: SupplierService = Depends(get_supplier_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Create a new supplier."""
    try:
        supplier_id = service.create(supplier.model_dump())
        return {"id": supplier_id, "message": "Supplier created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{supplier_id}")
async def update_supplier(
    supplier_id: int,
    supplier: SupplierUpdate,
    service: SupplierService = Depends(get_supplier_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Update a supplier."""
    try:
        data = supplier.model_dump()
        data["id"] = supplier_id
        success = service.update(data)
        if success:
            return {"message": "Supplier updated successfully"}
        raise HTTPException(status_code=400, detail="Update failed")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{supplier_id}")
async def delete_supplier(
    supplier_id: int,
    service: SupplierService = Depends(get_supplier_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Delete a supplier."""
    try:
        success = service.delete(supplier_id)
        if success:
            return {"message": "Supplier deleted successfully"}
        raise HTTPException(status_code=400, detail="Delete failed")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
