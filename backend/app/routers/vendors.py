"""Vendor router."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db import get_db
from app.repositories.vendor_repository import VendorRepository

router = APIRouter()


@router.get("")
async def get_vendors(
    city: Optional[str] = None,
    category: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get vendors, optionally filtered by city and category."""
    repository = VendorRepository(db)
    vendors = repository.get_vendors(city=city, category=category)
    return {"vendors": vendors, "total": len(vendors)}


@router.get("/{vendor_id}")
async def get_vendor(vendor_id: int, db: Session = Depends(get_db)):
    """Get a specific vendor by ID."""
    repository = VendorRepository(db)
    vendor = repository.get_vendor_by_id(vendor_id)
    if not vendor:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendor
